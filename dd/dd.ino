
char s;
void setup() {
  
  
  Serial.begin(9600);
  

}

void loop() 
{

while(Serial.available()>0)
{
  String s= Serial.readString();
  Serial.println(s);
  delay(500);
  
}

}
