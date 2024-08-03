/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JInternalFrame.java to edit this template
 */
package clases;

import java.util.ArrayList;
import static javax.swing.JOptionPane.showMessageDialog;

/**
 *
 * @author user
 */
public class IngresoDatos extends javax.swing.JInternalFrame {
    
    /**
     * Creates new form Ingreso_datos
     */
    public IngresoDatos() {
        
        initComponents();
    }
    public ArrayList<alumno> RegistroDeAlumnos = new ArrayList<>();
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    private String get__NumeroDni(){
        return txtNumDni.getText();
    }
    private String get__Nombres(){
        return txtNombres.getText();
    }
    private String get__Nota1(){
        int x = (int) txtNota1.getValue();
        return Integer.toString(x);
    }
    private String get__Nota2(){
        int x = (int) txtNota2.getValue();
        return Integer.toString(x);
    }
    private String get__Nota3(){
        int x = (int) txtNota3.getValue();
        return Integer.toString(x);
    }
    private String get__Nota4(){
        int x = (int) txtNota4.getValue();
        return Integer.toString(x);
    }
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        txtNumDni = new javax.swing.JTextField();
        txtNombres = new javax.swing.JTextField();
        lbDNI = new javax.swing.JLabel();
        lbNOMBRES = new javax.swing.JLabel();
        INDICACION = new javax.swing.JLabel();
        lbNOTA1 = new javax.swing.JLabel();
        lbNOTA2 = new javax.swing.JLabel();
        lbNOTA3 = new javax.swing.JLabel();
        lbNOTA4 = new javax.swing.JLabel();
        btnAgregar = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jLabel8 = new javax.swing.JLabel();
        lblNumRegistros = new javax.swing.JLabel();
        label = new javax.swing.JLabel();
        LabeltotalRegistros = new javax.swing.JLabel();
        txtPromedioNotas = new javax.swing.JLabel();
        txtNota1 = new javax.swing.JSpinner();
        txtNota2 = new javax.swing.JSpinner();
        txtNota3 = new javax.swing.JSpinner();
        txtNota4 = new javax.swing.JSpinner();

        setBackground(new java.awt.Color(153, 255, 204));
        setClosable(true);
        setResizable(true);
        setTitle("Ingreso de Datos");
        setMaximumSize(new java.awt.Dimension(703, 310));
        setMinimumSize(new java.awt.Dimension(703, 310));
        setName(""); // NOI18N

        txtNumDni.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        txtNumDni.setName("txtNumDni"); // NOI18N
        txtNumDni.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtNumDniKeyTyped(evt);
            }
        });

        txtNombres.setName("txtNombres"); // NOI18N
        txtNombres.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyTyped(java.awt.event.KeyEvent evt) {
                txtNombresKeyTyped(evt);
            }
        });

        lbDNI.setForeground(new java.awt.Color(102, 102, 102));
        lbDNI.setText("DNI:");
        lbDNI.setName("textDni"); // NOI18N

        lbNOMBRES.setForeground(new java.awt.Color(102, 102, 102));
        lbNOMBRES.setText("Nombres:");

        INDICACION.setForeground(new java.awt.Color(102, 102, 102));
        INDICACION.setText("Ingrese las 4 calificaciones del alumno para promediar su nota:");

        lbNOTA1.setForeground(new java.awt.Color(102, 102, 102));
        lbNOTA1.setText("Nota 1:");

        lbNOTA2.setForeground(new java.awt.Color(102, 102, 102));
        lbNOTA2.setText("Nota 2:");

        lbNOTA3.setForeground(new java.awt.Color(102, 102, 102));
        lbNOTA3.setText("Nota 3:");

        lbNOTA4.setForeground(new java.awt.Color(102, 102, 102));
        lbNOTA4.setText("Nota 4:");

        btnAgregar.setForeground(new java.awt.Color(102, 102, 102));
        btnAgregar.setText("Agregar");
        btnAgregar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAgregarActionPerformed(evt);
            }
        });

        jButton2.setForeground(new java.awt.Color(102, 102, 102));
        jButton2.setText("Cerrar");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        jLabel8.setName("txtError"); // NOI18N

        lblNumRegistros.setForeground(new java.awt.Color(102, 102, 102));
        lblNumRegistros.setText("Num. Registrados:");
        lblNumRegistros.setName("txtCantidadRegistro"); // NOI18N

        label.setForeground(new java.awt.Color(102, 102, 102));
        label.setText("Promedio de Notas:");
        label.setName("txtPromedioNotas"); // NOI18N

        LabeltotalRegistros.setForeground(new java.awt.Color(102, 102, 102));
        LabeltotalRegistros.setText("0");
        LabeltotalRegistros.setName("txtCantidadRegistro"); // NOI18N

        txtPromedioNotas.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        txtPromedioNotas.setForeground(new java.awt.Color(102, 102, 102));
        txtPromedioNotas.setText("0");
        txtPromedioNotas.setName("txtCantidadRegistro"); // NOI18N

        txtNota1.setModel(new javax.swing.SpinnerNumberModel(0, 0, 20, 1));
        txtNota1.setMaximumSize(new java.awt.Dimension(64, 22));

        txtNota2.setModel(new javax.swing.SpinnerNumberModel(0, 0, 20, 1));
        txtNota2.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        txtNota2.setMaximumSize(new java.awt.Dimension(64, 6));
        txtNota2.setName(""); // NOI18N
        txtNota2.setOpaque(true);

        txtNota3.setModel(new javax.swing.SpinnerNumberModel(0, 0, 20, 1));

        txtNota4.setModel(new javax.swing.SpinnerNumberModel(0, 0, 20, 1));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(26, 26, 26)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(btnAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, 152, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbDNI)
                                    .addComponent(txtNumDni, javax.swing.GroupLayout.PREFERRED_SIZE, 76, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(35, 35, 35)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbNOMBRES)
                                    .addComponent(txtNombres)))
                            .addComponent(INDICACION)
                            .addComponent(jLabel8)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(lblNumRegistros)
                                            .addComponent(LabeltotalRegistros, javax.swing.GroupLayout.PREFERRED_SIZE, 97, javax.swing.GroupLayout.PREFERRED_SIZE))
                                        .addGap(76, 76, 76))
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addGroup(layout.createSequentialGroup()
                                                .addComponent(lbNOTA1)
                                                .addGap(0, 0, Short.MAX_VALUE))
                                            .addComponent(txtNota1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addGroup(layout.createSequentialGroup()
                                                .addGap(31, 31, 31)
                                                .addComponent(lbNOTA2))
                                            .addGroup(layout.createSequentialGroup()
                                                .addGap(18, 18, 18)
                                                .addComponent(txtNota2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                        .addGap(10, 10, 10)))
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                        .addComponent(txtPromedioNotas, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(label))
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                        .addComponent(jButton2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                            .addGap(12, 12, 12)
                                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                .addComponent(lbNOTA3)
                                                .addComponent(txtNota3, javax.swing.GroupLayout.PREFERRED_SIZE, 72, javax.swing.GroupLayout.PREFERRED_SIZE))
                                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                .addComponent(lbNOTA4)
                                                .addComponent(txtNota4, javax.swing.GroupLayout.PREFERRED_SIZE, 82, javax.swing.GroupLayout.PREFERRED_SIZE)))))))
                        .addGap(28, 28, 28))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lbDNI)
                    .addComponent(lbNOMBRES))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtNumDni, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtNombres, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(12, 12, 12)
                .addComponent(INDICACION)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lbNOTA1)
                    .addComponent(lbNOTA2)
                    .addComponent(lbNOTA3)
                    .addComponent(lbNOTA4))
                .addGap(12, 12, 12)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtNota1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtNota2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtNota3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtNota4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton2, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 26, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblNumRegistros)
                    .addComponent(label))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(LabeltotalRegistros, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtPromedioNotas, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(17, 17, 17)
                .addComponent(jLabel8)
                .addContainerGap(28, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents
    
    private void btnAgregarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAgregarActionPerformed
        // TODO add your handling code here:

        if(fn__validarCampoVacios().equals("")){
            if(get__NumeroDeRegistros() == 0){                
                objAlumno__Nuevo();                
            }else{
                if (fn__validarDNI(get__NumeroDni()) == true) {
                    showMessageDialog(null, "El DNI " + get__NumeroDni() + " ya se encuentra Registrado");
                    Limpiar();
                } 
                else {
                    objAlumno__Nuevo();
                }
            }  
        }else{
            showMessageDialog(null, fn__validarCampoVacios());
        }         
    }//GEN-LAST:event_btnAgregarActionPerformed
    public void objAlumno__Nuevo(){
        alumno newObjAlumno = new alumno(get__NumeroDni(), get__Nombres(),get__Nota1(),get__Nota2(),get__Nota3(),get__Nota4());
        RegistroDeAlumnos.add(newObjAlumno);
        if (newObjAlumno.getNotaPromedio() > 11){
            showMessageDialog(null, "Hola " + get__Nombres() + "\nUd APROBO y su nota es: " + newObjAlumno.getNotaPromedio());
        }else{
            showMessageDialog(null, "Hola " + get__Nombres() + "\nUd NO APROBO y su nota es: " + newObjAlumno.getNotaPromedio());
        }
        LabeltotalRegistros.setText(Integer.toString(get__NumeroDeRegistros()));
        txtPromedioNotas.setText(get__promedioNotas());
        Limpiar();
    }
    public int get__NumeroDeRegistros(){
        return RegistroDeAlumnos.size();
    }
    public String get__promedioNotas(){
        double ponderado = 0;
        String resultado;
        for(alumno item:RegistroDeAlumnos){
            ponderado = item.getNotaPromedio() + ponderado;
        }
        resultado = Integer.toString((int)ponderado / get__NumeroDeRegistros());
        return resultado;
    }
    private void txtNumDniKeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtNumDniKeyTyped
        // TODO add your handling code here:
        if(get__NumeroDni().length() >= 8){
            evt.consume();
        }
        if((evt.getKeyChar() <= 48 && evt.getKeyChar() >= 57) == true){
            evt.consume();
        }
    }//GEN-LAST:event_txtNumDniKeyTyped

    private void txtNombresKeyTyped(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtNombresKeyTyped
        // TODO add your handling code here:
        if((evt.getKeyChar() >= 33 && evt.getKeyChar() <= 64) == true){
            evt.consume(); // No permite Ingresar Numeros
        }
    }//GEN-LAST:event_txtNombresKeyTyped

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        // TODO add your handling code here:
        int x = get__NumeroDeRegistros();
        System.out.print(x);
        if(get__NumeroDeRegistros() == 0){
            showMessageDialog(null,"No se realizo ningun Registro\nBuen dia!!!");
        }else{
            showMessageDialog(null,"Se realizaron " + 
                Integer.toString(get__NumeroDeRegistros()) +
                "\nel Promedio total de los registros es: " + 
                get__promedioNotas());
        }
        
        this.dispose();
    }//GEN-LAST:event_jButton2ActionPerformed
    public boolean fn__validarDNI(String dni){
        boolean validate = false;
        for (alumno objAlumno_ : RegistroDeAlumnos) {
            if (objAlumno_.getDni().equals(dni)) {
                validate = true;
                break;
            } 
        }
        return validate;
    }
    public String fn__validarCampoVacios(){
        if (get__NumeroDni().equals("")) {
            txtNumDni.requestFocus();
            return "El campo DNI esta vacio!";
        }
        if(get__NumeroDni().length() != 8){
            txtNumDni.requestFocus();
            return "El DNI tiene que ser 8 Digitos Profavor Revisar";
        }        
        if (get__Nombres().equals("")) {
            txtNombres.requestFocus();
            return "El campo Nombre esta vacio!";
        }
        if (get__Nota1().equals("")) {
            txtNota1.requestFocus();
            return "El campo Nota 1 esta vacio!";
        }
        if (get__Nota2().equals("")) {
            txtNota2.requestFocus();
            return "El campo Nota 2 esta vacio!";
        }
        if (get__Nota3().equals("")) {
            txtNota3.requestFocus();
            return "El campo Nota 3 esta vacio!";
        }
        if (get__Nota4().equals("")) {
            txtNota4.requestFocus();
            return "El campo Nota 4 esta vacio!";
        }
        return "";
    }
//    public static char StringToChar(String s) {
//        return (char)s.codePointAt(0);
//    }
    public void Limpiar(){
        txtNumDni.setText("");
        txtNombres.setText("");
        txtNota1.setValue(0);
        txtNota2.setValue(0);
        txtNota3.setValue(0);
        txtNota4.setValue(0);
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel INDICACION;
    private javax.swing.JLabel LabeltotalRegistros;
    private javax.swing.JButton btnAgregar;
    private javax.swing.JButton jButton2;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel label;
    private javax.swing.JLabel lbDNI;
    private javax.swing.JLabel lbNOMBRES;
    private javax.swing.JLabel lbNOTA1;
    private javax.swing.JLabel lbNOTA2;
    private javax.swing.JLabel lbNOTA3;
    private javax.swing.JLabel lbNOTA4;
    private javax.swing.JLabel lblNumRegistros;
    private javax.swing.JTextField txtNombres;
    private javax.swing.JSpinner txtNota1;
    private javax.swing.JSpinner txtNota2;
    private javax.swing.JSpinner txtNota3;
    private javax.swing.JSpinner txtNota4;
    private javax.swing.JTextField txtNumDni;
    private javax.swing.JLabel txtPromedioNotas;
    // End of variables declaration//GEN-END:variables

}
