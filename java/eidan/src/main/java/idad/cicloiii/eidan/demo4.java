
package idad.cicloiii.eidan;

import java.util.Scanner;

/**
 *
 * @author IDAT
 */
public class demo4 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingrese un numero: ");
        int num1;
        num1 = entrada.nextInt();
        switch(num1){
            case 1 -> System.out.println("Lunes");
            case 2 -> System.out.println("Martes");
            case 3 -> System.out.println("Miercoles");
            case 4 -> System.out.println("Jueves");
            case 5 -> System.out.println("Viernes");
            case 6 -> System.out.println("Sabado");
            case 7 -> System.out.println("Domingo");
            default -> System.out.println("El dia ingresado no representa un dia de semana");
        }
        
    }

}
