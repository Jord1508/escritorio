package idad.cicloiii.ec_2;

import clases.Empleado;
import java.util.Scanner;

public class EC_2 {

    public static void main(String[] args) {
        //System.out.println("Hello World!");
        //Scanner entrada = new Scanner(System.in);
        Empleado empleado = new Empleado();
        Scanner entrada = new Scanner(System.in);    
        System.out.println("Ingrese su DNI");
        empleado.setDni(entrada.next());
        System.out.println("Dato ingresado " + empleado.getDni());
    }
    
    
}
