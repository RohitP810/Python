
#define HX_DOUT  18
#define HX_CLK 14
#define button 35


#include "HX711.h"

long raw;


HX711 loadcell;


void setup() {
pinMode(button , INPUT);
loadcell.begin(HX_DOUT, HX_CLK);
Serial.begin(9600);

}

void loop() {
if(!digitalRead(button))
{
delay(2000);
raw=loadcell.read_average(100);
Serial.print(raw);
Serial.println(",");
}
}
