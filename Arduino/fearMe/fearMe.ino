#include <Wire.h>
#include <Adafruit_RGBLCDShield.h>

// These #defines make it easy to set the backlight color
#define RED 0x1
#define GREEN 0x2
#define YELLOW 0x3
#define BLUE 0x4
#define VIOLET 0x5
#define TEAL 0x6
#define WHITE 0x7

Adafruit_RGBLCDShield lcd = Adafruit_RGBLCDShield();

#include <SoftwareSerial.h>

#define rxPin 9    // Serial input (connects to Emic 2 SOUT)
#define txPin 8    // Serial output (connects to Emic 2 SIN)
#define ledPin 13  // Most Arduino boards have an on-board LED on this pin


// set up a new serial port
SoftwareSerial emicSerial =  SoftwareSerial(rxPin, txPin);

//char inData[20] = "u:Steve's p:iPhone"; // Allocate some space for the string
char inData[20];
char inChar; // Where to store the character read
byte index = 0; // Index into array; where to store the character

//String user = "u:Steve";
//String phone = "p:iPhone";

const float ver = 0.06;

void setup() {
  Serial.begin(9600);
  Serial.write("Power On");
  Serial.end();

  lcd.begin(16, 2);
  lcd.setBacklight(WHITE);
  lcd.print("Welcome to: ");
  lcd.setCursor(0,1);
  lcd.print("fearMe v");
  lcd.print(ver);
  delay(3000);
  lcd.clear();
    // define pin modes
  pinMode(ledPin, OUTPUT);
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  
  // set the data rate for the SoftwareSerial port
  emicSerial.begin(9600);
    digitalWrite(ledPin, LOW);  // turn LED off
 
  /*
    When the Emic 2 powers on, it takes about 3 seconds for it to successfully
    intialize. It then sends a ":" character to indicate it's ready to accept
    commands. If the Emic 2 is already initialized, a CR will also cause it
    to send a ":"
  */
  emicSerial.print('\n');             // Send a CR in case the system is already up
  while (emicSerial.read() != ':');   // When the Emic 2 has initialized and is ready, it will send a single ':' character, so wait here until we receive it
  delay(10);                          // Short delay
  //emicSerial.print('N1');
  //while (emicSerial.read() != ':');   // When the Emic 2 has initialized and is ready, it will send a single ':' character, so wait here until we receive it
  //delay(10);                          // Short delay  
  //emicSerial.print('\n');             // Send a CR in case the system is already up
  emicSerial.flush();                 // Flush the receive buffer
  delay(500);    // 1/2 second delay
  // Speak some text
  emicSerial.print('S');
  emicSerial.print("Hello Pascal, welcome to Fear Me. This is an early version. Are you afraid? I am. But the most fearing thing will be the Box I will be living in");
  emicSerial.print('\n');

  digitalWrite(ledPin, HIGH);         // Turn on LED while Emic is outputting audio
  while (emicSerial.read() != ':');   // Wait here until the Emic 2 responds with a ":" indicating it's ready to accept the next command
  digitalWrite(ledPin, LOW);
  delay(500);    // 1/2 second delay
}

void loop() {
  Serial.begin(9600);

     while(Serial.available() > 0) // Don't read unless
                                                  // there you know there is data
   {
       if(index < 19) // One less than the size of the array
       {
           inChar = Serial.read(); // Read a character
           inData[index] = inChar; // Store it
           index++; // Increment where to write next
           inData[index] = '\0'; // Null terminate the string
       }
  }

String phoneSpecs = inData;

delay(1000);
connPhone("Steve Clement", "iPhone");
delay(10000);

//if ( phoneSpecs.length() > 3 ){
//  spinner(100,0);
//  lcd.print("len.str: ");
//  lcd.print(phoneSpecs.length());
//  lcd.setCursor(0,1);
//  lcd.print("data: ");
//  lcd.print(phoneSpecs);
//  char inData[20];
//  String phoneSpecs = "";
//  Serial.end();
//  delay(1000);
//  lcd.clear();
//} else {
//  lcd.clear();
//  lcd.print("No Data :(");
//  delay(100);
//}

//  for (int i = 0; i < phoneSpecs.length() ; i++){
//  lcd.print(phoneSpecs[i]);
//  delay(1000); 
  // lcd.clear();
//  }
  

 
  //lcd.setBacklight(YELLOW);
  //spinner(500,1);
  //lcd.setBacklight(TEAL);
  //lcd.setBacklight(YELLOW);
  //lcd.setBacklight(VIOLET);
  //lcd.setBacklight(BLUE);
  //lcd.setBacklight(WHITE);

}

void connPhone(String user, String phone){
  lcd.clear();
  lcd.setBacklight(GREEN);
  lcd.setCursor(0, 0);
  spinner(250,0);
  spinner(250,0);
  spinner(250,0);
  lcd.print("Hi ");
  lcd.print(user);
  delay(3000);
  lcd.setCursor(0, 0);
  lcd.clear();
  lcd.print("Your:");
  spinner(250,1);
  spinner(250,1);
  lcd.setCursor(0, 1);
  lcd.print(phone);
  lcd.print(" is safe now!");
  lcd.setBacklight(RED);

  delay(5000);
  lcd.clear();
}

void spinner(int spinSpeed, int line){
  lcd.setCursor(0, line);
  delay(spinSpeed);
  lcd.print("/");

  lcd.setCursor(0, line);
  delay(spinSpeed);
  lcd.print("-");

  lcd.setCursor(0, line);
  delay(spinSpeed);
  lcd.write(0b10100100);

  lcd.setCursor(0, line);
  delay(spinSpeed);
  lcd.print("|");
}
