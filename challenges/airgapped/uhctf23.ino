#define SOLO 14
#define R 27
#define G 25
#define B 26

char flag[] = "UHCTF{c0l0r$}";
int flaglength = 13;


char flag_2[] = "UHCTF(dit-dah-dah-F4DE3)";
char flag_morse[] = "..- .... -.-. - ..-. -.--. -.. .. - -....- -.. .- .... -....- -.. .- .... -....- ..-. ....- -.. . ...-- -.--.-";

// Morse code timings
int _short = 100;
int _long = 300;
int space = 400;

// RGB timing
int rgb_delay = 100;
int begin_multiplier = 4;

void morseCode(){
  for (int i =0; i < strlen(flag_morse) ; i++){
    
  unsigned char c = flag_morse[i];
    if (c == '.'){
      digitalWrite(SOLO,1);
      delay(_short);
      digitalWrite(SOLO,0);
    }
    else if (c == '-'){
      digitalWrite(SOLO,1);
      delay(_long);
      digitalWrite(SOLO,0);
    }
    else if (c == ' '){
         delay(_long);
    }
    delay(_short);

    Serial.print(char(c));
  }
  

  delay(5000);
  Serial.println();
  
}

int currentColor; // 0 for red, 1 for green, 2 for blue

void nextColor(int b){
  if (!b){
    currentColor += 1;
  } else {
    currentColor -= 1;
  }
  if (currentColor < 0){
    currentColor = 2;
  }
  if (currentColor > 2){
    currentColor = 0;
  }

  if (currentColor == 0){
   digitalWrite(R, 1);
   digitalWrite(G, 0);
   digitalWrite(B, 0);
  }
  
  if (currentColor == 1){
   digitalWrite(R, 0);
   digitalWrite(G, 1);
   digitalWrite(B, 0);
  }
  
  if (currentColor == 2){
   digitalWrite(R, 0);
   digitalWrite(G, 0);
   digitalWrite(B, 1);
  }

}


void RGBCode(){
   currentColor = 0;
  digitalWrite(R, 1);
   digitalWrite(G, 0);
   digitalWrite(B, 0);
   
   delay(rgb_delay*begin_multiplier); 
for (int i =0; i < strlen(flag) ; i++){

  unsigned char c = flag[i];
  
  for (unsigned int mask = 0x80; mask != 0; mask >>= 1) {

    if (c & mask) {
        Serial.print("1");
        nextColor(1);
    }
    else {
        Serial.print("0");
        nextColor(0);
    }
    
   delay(rgb_delay); 
  }
  Serial.print(" ");
  Serial.print(char(c));
 delay(rgb_delay);
 Serial.println();
  
 }
  digitalWrite(R, 0);
   digitalWrite(G, 0);
   digitalWrite(B, 0);
   

}

void setup(){
    Serial.begin(115200);
    pinMode(SOLO, OUTPUT);
    pinMode(R, OUTPUT);
    pinMode(G, OUTPUT);
    pinMode(B, OUTPUT);
    Serial.println("Setup done");
}

void loop()
{
 
 RGBCode();

 morseCode();

}
