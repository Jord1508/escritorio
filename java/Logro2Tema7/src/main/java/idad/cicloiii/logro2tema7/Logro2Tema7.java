
package idad.cicloiii.logro2tema7;

import clases.Alumno;


public class Logro2Tema7 {

    public static void main(String[] args) {
//        System.out.println("Hello World!");
        Alumno alu = new Alumno("79942587");
        alu.setNombre("Joselyn");
        alu.setApellidoPaterno("Barrios");
        alu.setApellidoMaterno("Lima");
        alu.setSexo("F");
        alu.setFechaNacimiento("21/05/1998");
        
        System.out.println("Alumno: " + alu.getNombreCompleto() + ". Su edad es: " + alu.getEdad());
    }
}
