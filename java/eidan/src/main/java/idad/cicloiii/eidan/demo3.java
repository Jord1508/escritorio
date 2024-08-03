package idad.cicloiii.eidan;

import java.util.Scanner;

/**
 *
 * @author IDAT
 */
public class demo3 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num1;
        int num2;
        
        System.out.print("Ingrese un numero: ");
        num1 = entrada.nextInt();
        
        System.out.println("");
        
        System.out.print("Ingrese otro numero: ");
        num2 = entrada.nextInt();
        
        
        if(num1 != num2){
            if( num1 > num2){
                System.out.println("El primer numero es mayor");
            }
            else{
                System.out.println("El segundo numero es mayor");
            }
        }
        else{
            System.out.println("Ambos numeros son iguales");
        }
        
    }
}
