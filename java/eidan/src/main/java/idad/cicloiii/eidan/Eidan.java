package idad.cicloiii.eidan;

import java.io.IOException;

/**
 *
 * @author IDAT
 */
public class Eidan {

    public static void main(String[] args) throws IOException {
        int inCaracter;
        System.out.println("Ingrese un caracter");
        
        inCaracter = System.in.read();
        System.out.println("Ud ingreso: ");
        System.out.println(inCaracter);
        
    }
}
