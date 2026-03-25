int m1=2;
int m2=3;
int m3=4;
int m4=5;
void setup() {
Serial.begin(9600);
pinMode(m1,OUTPUT);
pinMode(m2,OUTPUT);
pinMode(m3,OUTPUT);
pinMode(m4,OUTPUT);
digitalWrite(m1,1);
digitalWrite(m2,0);
digitalWrite(m3,1);
digitalWrite(m4,0);
}
void loop() {
  digitalWrite(m1,1);
digitalWrite(m2,0);
digitalWrite(m3,1);
digitalWrite(m4,0);
  if(Serial.available())
  {
    int x=Serial.read();
    if(x=='1')
    {
      digitalWrite(m1,0);
      digitalWrite(m2,0);
      digitalWrite(m3,0);
      digitalWrite(m4,0);
      while(1);
    }
  }
}
