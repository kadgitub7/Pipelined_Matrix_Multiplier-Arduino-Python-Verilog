import serial
import time

# Change 'COM3' to your actual port (e.g., '/dev/ttyACM0' on Linux/Mac)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=2)

# Give Arduino time to reset after opening serial
time.sleep(2)

matrices = []

for i in range(2):
    data = arduino.readline().decode().strip()
    if data:
        numbers = [int(x) for x in data.split(',') if x.strip() != '']
        matrices.append(numbers)

arduino.close()

matrix_1 = [matrices[0][i:i+4] for i in range(0, 16, 4)]
matrix_2 = [matrices[1][i:i+4] for i in range(0, 16, 4)]

print("\nMatrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

# Save matrices into hex files to be read in Verilog
def save_matrix_to_hex(matrix, filename):
    with open(filename, "w") as f:
        for val in matrix:
            f.write(f"{val:02x}\n")  # 2-digit hex values

save_matrix_to_hex(matrices[0], "matrix1.hex")
save_matrix_to_hex(matrices[1], "matrix2.hex")
print("Saved matrix1.hex and matrix2.hex")

time.sleep(90) # Wait for Verilog simulation to complete

# Read the result
try:
    with open("matrix_c_output.txt", "r") as f:
        result_values = [int(line.strip()) for line in f if line.strip()]
except FileNotFoundError:
    print("Error: matrix_c_output.txt not found. Make sure Verilog has run.")
    exit(1)

# Convert to 4x4 matrix
matrix_c = [result_values[i:i+4] for i in range(0, 16, 4)]

print("\nMatrix C (Result of A x B):")
for row in matrix_c:
    print(" ".join(f"{val:4d}" for val in row))