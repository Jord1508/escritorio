
package idad.cicloiii.tareatemaiii;

import java.util.Scanner;

public class ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num;
        System.out.println("Ingrese un numero: ");
        num = entrada.nextInt();
        Analizador(num);
        
    }
    
    private static void Analizador(int numero){
        if (numero % 2 == 0){
            System.out.println("Es par el numero ingresado");
        }else{
            System.out.println("Es impar el numero ingresado");
        }
    }
}
