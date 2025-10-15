void setup() {
  Serial.begin(9600); // Initialize serial communication for output
  randomSeed(analogRead(A0)); // Seed the random number generator using analogRead on unconnected pin A0
  for(int j = 0; j<2; j++){
    for (int i = 0; i<16; i++){
      int r = random(0,10);
      Serial.print(r);

      if(r<15) Serial.print(",");
  
    }
    Serial.println();
  }
  
}

void loop() {
  
}
