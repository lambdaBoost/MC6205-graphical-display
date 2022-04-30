
#include <MS6205.h>


int LEFT_BUTTON_PIN = 16;
int RIGHT_BUTTON_PIN = 4;
int ROTATE_PIN = 17;

int const shiftRegisterLatchPin  = 15; // GPIO15 = Pin D8 on NodeMCU boards. Pin 12 on 74HC595.
int const shiftRegisterClockPin  = 14; // GPIO14 = Pin D5 on NodeMCU boards. Pin 11 on 74HC595.
int const shiftRegisterDataPin   = 13; // GPIO13 = Pin D7 on NodeMCU boards. Pin 14 on 74HC595.
int const displaySetPositionPin  = 12; // GPIO12 = Pin D6 on NodeMCU boards. Pin 16A on MS6205.
int const displaySetCharacterPin = 2;  // GPIO2  = Pin D4 on NodeMCU boards. Pin 16B on MS6205.
int const displayClearPin        = 5;  // GPIO5  = Pin D1 on NodeMCU boards. Pin 18A on MS6205.


MS6205 display(shiftRegisterLatchPin, shiftRegisterClockPin, shiftRegisterDataPin, displaySetPositionPin, displaySetCharacterPin, displayClearPin);

int tm=0;

int d[ 10 ][ 16 ] = { { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
                      { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 }};

int rowSums[10] = {0,0,0,0,0,0,0,0,0,0};

int xpos = 7;
int ypos = 0;


void setup() {

  pinMode(LEFT_BUTTON_PIN, INPUT_PULLUP);
  pinMode(RIGHT_BUTTON_PIN, INPUT_PULLUP);
  pinMode(ROTATE_PIN, INPUT_PULLUP);
  
   display.clear();
}


  int piece[4][4] = {{0,0,0,0},
                 {0,0,0,0},
                 {0,0,0,0},
                 {1,1,1,1}};


void loop() {
  
  display.clear();

//movement
int left_button_state = digitalRead(LEFT_BUTTON_PIN);
int right_button_state = digitalRead(RIGHT_BUTTON_PIN);

if(left_button_state == 0){
  xpos--;
}

if(right_button_state == 0){
  xpos++;
}

if(xpos>12){
  xpos=12;
}

if(xpos <0){
  xpos = 0;
}


//rotate piece
int rotate_button_state = digitalRead(ROTATE_PIN);

if(rotate_button_state == 0){
  int tempPiece[4][4];
    for(int i=0;i<=3;i++){
    for(int j=0;j<=3;j++){
  
      tempPiece[i][j] = piece[i][j];
    }
  }

  
  for(int i=0;i<=3;i++){
    for(int j=0;j<=3;j++){
  
      piece[i][j] =tempPiece[j][i];
    }
  }
}

//stack blocks

        for (int s=0; s<=3; s++){
          if (piece[3][s]==1 and d[(ypos +3 )][xpos + s] == 1){

                    for (int j=0; j<=3; j++){
                      for (int k=0; k<=3; k++){
                        if (piece[j][k]==1){

                           d[(ypos-1) + j][xpos+k] = 1;
                              }
                            }
                          }

                 xpos = 7;
                 ypos=-3;

                 //generate new piece. This is a monumentally stupid way of doing it but
     //i can't be bothered figuring out arrays and pointers and all that nonsense.
     //it's not the 1980's...just use numpy.
          int pieceIndex = random(0,7);

        //right L
          if(pieceIndex == 0){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=1; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=1; piece[2][1]=0;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }

        //left L
          if(pieceIndex == 1){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=1;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }

        //left squiggle
          if(pieceIndex == 2){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=1;piece[2][2]=1;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }
        //right squiggle
          if(pieceIndex == 3){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=1; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=0; piece[3][1]=1;piece[3][2]=1;piece[3][3]=0;
          }

       //square
          if(pieceIndex == 4){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=1; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }

      //line
          if(pieceIndex == 5){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=0;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=1;piece[3][3]=1;
          }

       //Tblock
          if(pieceIndex == 6){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=1;piece[3][3]=0;
          }

          
          }

  }




//bottom of screen
  if(ypos >=7){

        for (int r=0; r<=3; r++){
        for (int s=0; s<=3; s++){
          if (piece[r][s]==1){

            d[6 + r][xpos+s] = 1;
          }
        }
      }

    ypos = -3;
    xpos = 7;

     //generate new piece. This is a monumentally stupid way of doing it but
     //i can't be bothered figuring out arrays and pointers and all that nonsense.
     //it's not the 1980's...just use numpy.
 int pieceIndex = random(0,7);

        //right L
          if(pieceIndex == 0){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=1; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=1; piece[2][1]=0;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }

        //left L
          if(pieceIndex == 1){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=1;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }

        //left squiggle
          if(pieceIndex == 2){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=1;piece[2][2]=1;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }
        //right squiggle
          if(pieceIndex == 3){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=1; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=0; piece[3][1]=1;piece[3][2]=1;piece[3][3]=0;
          }

       //square
          if(pieceIndex == 4){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=1; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=0;piece[3][3]=0;
          }

      //line
          if(pieceIndex == 5){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=0;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=1;piece[3][3]=1;
          }

             //Tblock
          if(pieceIndex == 6){
           piece[0][0]=0; piece[0][1]=0;piece[0][2]=0;piece[0][3]=0;
           piece[1][0]=0; piece[1][1]=0;piece[1][2]=0;piece[1][3]=0;
           piece[2][0]=0; piece[2][1]=1;piece[2][2]=0;piece[2][3]=0;
           piece[3][0]=1; piece[3][1]=1;piece[3][2]=1;piece[3][3]=0;
          }

  }


 

//draw play area
  for(int i=0; i<=10; i++){
    for(int j=0; j<=15; j++){

      if(d[i][j] == 1){
        display.writeBlock(j,i);
        //delay(1);


    }
    }
  }







//draw falling block

 for (int r=0; r<=3; r++){
     for (int s=0; s<=3; s++){
         if (piece[r][s]==1){

            display.writeBlock(xpos + s, ypos+r);
          }
        }
      }

 //clear rows
for (int r = 9; r>=0; r--){

  int rowSum = 0;
  for(int c = 2; c<=13; c++){

    if(d[r][c] == 1){
      rowSum ++;
    }
  }

  if(rowSum >= 12){
    
      for (int R=r; R>=1; R--){
          for(int C=0; C<=15; C++){
            d[R][C] = d[R-1][C];
            }
    }
      

    
  }
  
}

 if((millis() - tm )>500){
 ypos++;
 tm=millis();
 }
 
 delay(200);
 
}
