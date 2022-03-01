void setup(){
    pinMode(10, OUTPUT);//Define a saída do sinal
    Serial.begin(115200);//Inicia a Serial
}
void loop(){
    int valorRecebido;
    if(Serial.available()){
        valorRecebido = Serial.read();
        if(valorRecebido == '0'){//Caso o valor do sensor seja 0, desligue a lâmpada, caso contrário, ligue
            digitalWrite(10, 'LOW');
        }else{
            digitalWrite(10, 'HIGH');
        }
    }
}