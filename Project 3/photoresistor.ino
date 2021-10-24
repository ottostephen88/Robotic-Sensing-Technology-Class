

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  
}



void loop() {
  // put your main code here, to run repeatedly:
  int offset=600;
int state;
int readin;
char rec[] = "OFF";
state = 0;
readin = analogRead(A0);
Serial.println(readin);
if(readin > offset)
{
  Serial.print("Light off");
  }
  else
  {
    Serial.print("Light on");
    }
delay(10);
}
