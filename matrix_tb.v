module matrix_loader;
    reg [7:0] matrix1 [0:15]; // Allocate memory for 16 elements each 8 bits
    reg [7:0] matrix2 [0:15]; 
    reg [15:0] matrix_c [0:15]; // Resultant matrix with 16-bit elements
    integer i,j,k, file;
    // This is where we are reading the two files for values
    initial begin
        $readmemh("matrix1.hex", matrix1);
        $readmemh("matrix2.hex", matrix2);

        $display("--- Loaded Hex Values ---");

        for (i = 0; i < 16; i = i + 1) begin
            $display("matrix1[%0d]: %h", i, matrix1[i]);
            $display("matrix2[%0d]: %h", i, matrix2[i]);
        end
        for (i = 0; i < 4; i++) begin // Row index of A
            for (j = 0; j < 4; j++) begin // Col index of B
            matrix_c[i*4 + j] = 0;
                for (k = 0; k < 4; k++) begin
                    matrix_c[i*4 + j] = matrix_c[i*4 + j] +
                    matrix1[i*4 + k] * matrix2[k*4 + j];
                end
            end
        end

        $display("--- Matrix C (Result) ---");
        for (i = 0; i < 16; i = i + 1) begin
            $display("matrix_c[%0d] = %d", i, matrix_c[i]);
        end

        file = $fopen("matrix_c_output.txt", "w"); // Open in write mode

        if (file) begin
            $display("Writing matrix_c to matrix_c_output.txt...");
            for (i = 0; i < 16; i = i + 1) begin
                $fdisplay(file, "%d", matrix_c[i]); // Write each value on a new line
            end
        $fclose(file); // Close the file
        end else begin
            $display("ERROR: Failed to open file for writing.");
        end
    end
endmodule