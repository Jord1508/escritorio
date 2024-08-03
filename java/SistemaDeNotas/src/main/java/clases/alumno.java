
package clases;

public class alumno {
    private String dni;
    private String nombres;
    private String nota1;
    private String nota2;
    private String nota3;
    private String nota4;
    
    public alumno(String dni){
        this.dni = dni;
    }
    public alumno(String dni,String nombres,String nota1,String nota2,String nota3,String nota4){
        this.dni = dni;
        this.nombres = nombres;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
        this.nota4 = nota4;
    }
    /**
     * @return the dni
     */
    public String getDni() {
        return dni;
    }

    /**
     * @param dni the dni to set
     */
    public void setDni(String dni) {
        this.dni = dni;
    }

    /**
     * @return the nombres
     */
    public String getNombres() {
        return nombres;
    }

    /**
     * @param nombres the nombres to set
     */
    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    /**
     * @return the nota1
     */
    public String getNota1() {
        return nota1;
    }

    /**
     * @param nota1 the nota1 to set
     */
    public void setNota1(String nota1) {
        this.nota1 = nota1;
    }

    /**
     * @return the nota2
     */
    public String getNota2() {
        return nota2;
    }

    /**
     * @param nota2 the nota2 to set
     */
    public void setNota2(String nota2) {
        this.nota2 = nota2;
    }

    /**
     * @return the nota3
     */
    public String getNota3() {
        return nota3;
    }

    /**
     * @param nota3 the nota3 to set
     */
    public void setNota3(String nota3) {
        this.nota3 = nota3;
    }

    /**
     * @return the nota4
     */
    public String getNota4() {
        return nota4;
    }

    /**
     * @param nota4 the nota4 to set
     */
    public void setNota4(String nota4) {
        this.nota4 = nota4;
    }
    
    public double getNotaPromedio(){
        double resultado;
        int num1 = Integer.parseInt(nota1);
        int num2 = Integer.parseInt(nota2);
        int num3 = Integer.parseInt(nota3);
        int num4 = Integer.parseInt(nota4);
        resultado = num1 * 0.05 + num2 * 0.15 + num3 * 0.3 + num4 * 0.5;
        return resultado;
    }
    
}
