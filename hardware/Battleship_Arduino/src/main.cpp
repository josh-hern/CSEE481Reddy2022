

#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7789.h> // Hardware-specific library for ST7789
#include <SPI.h>

#include <Game.h>
#include <Grid.h>

// Because of the limited number of pins available on the Circuit Playground Boards
// Software SPI is used
#define TFT_CS        14 
#define TFT_RST       32 // Or set to -1 and connect to Arduino RESET pin
#define TFT_DC        33 
//#define TFT_BACKLIGHT PIN_A3 // Display backlight pin

#define TFT_MOSI      23  // Data out
#define TFT_SCLK      18  // Clock out
Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);

void testdrawtext(char *text, uint16_t color) {
  tft.setCursor(0, 0);
  tft.setTextColor(color);
  tft.setTextWrap(true);
  tft.print(text);
}


void tftPrintTest() {
  tft.setTextWrap(false);
  tft.fillScreen(ST77XX_BLACK);
  tft.setCursor(0, 30);
  tft.setTextColor(ST77XX_RED);
  tft.setTextSize(1);
  tft.println("Hello World!");
  tft.setTextColor(ST77XX_YELLOW);
  tft.setTextSize(2);
  tft.println("Hello World!");
  tft.setTextColor(ST77XX_GREEN);
  tft.setTextSize(3);
  tft.println("Hello World!");
  tft.setTextColor(ST77XX_BLUE);
  tft.setTextSize(4);
  tft.print(1234.567);
  delay(1500);
  tft.setCursor(0, 0);
  tft.fillScreen(ST77XX_BLACK);
  tft.setTextColor(ST77XX_WHITE);
  tft.setTextSize(0);
  tft.println("Hello World!");
  tft.setTextSize(1);
  tft.setTextColor(ST77XX_GREEN);

  tft.print(8675309, HEX); // print 8,675,309 out in HEX!
  tft.println(" Print HEX!");
  tft.println(" ");
  tft.setTextColor(ST77XX_WHITE);
  tft.println("Sketch has been");
  tft.println("running for: ");
  tft.setTextColor(ST77XX_MAGENTA);
  tft.print(millis() / 1000);
  tft.setTextColor(ST77XX_WHITE);
  tft.print(" seconds.");
}



#include <Input.h>

Game* game;
extern UserInputs* inputs;

void setup(){

  Serial.begin(115200);
  Serial.println("Initializing inputs");
  inputs = new UserInputs();
  
  Serial.println("Initializing screen");
  tft.init(135, 240); 
  tft.fillScreen(COLOR_LIGHT_BLUE);

  Serial.println("Creating game");
  GameConfiguration* conf = new GameConfiguration();
  game = new Game(&tft, conf, inputs);

  game->draw();
  
}


void loop(){

  game->draw();

  vTaskDelay(pdMS_TO_TICKS(100));

}