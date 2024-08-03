using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Examen3
{
    public partial class Form1 : Form
    {
        private int codigo = 0;
        private ArrayList listaAlumnos = new ArrayList();
        public Form1()
        {
            InitializeComponent();
        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            int n = dataGridView1.CurrentCell.RowIndex;
            label1.Text = "" + n;
            int ef = 0;
            foreach(Estudiante elem in listaAlumnos)
            {
                if (ef == n)
                {
                    txtNombre.Text = elem.Nombre;
                    break;
                }
                ef++;
            }
            
        }
        

        private void Form1_Load(object sender, EventArgs e)
        {
            
            for (int i = 7; i <= 10; i++)
            {
                txtClase.Items.Add(" " +i + " th clase");
            }
            txtClase.SelectedIndex = 0;

        }
        private void nuevoEstudiante()
        {

            codigo = codigo + 1;
            string Fecha = txtFecha.Value.ToShortDateString();
            Estudiante est = new Estudiante(codigo, 
                txtNombre.Text,
                txtEdad.Text, txtCelular.Text, txtEmail.Text, GetGenero(), Fecha, txtClase.Text);

            listaAlumnos.Add(est);
            Limpiar();
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {

            nuevoEstudiante();
            mostrarItems();


        }
        public string GetGenero()
        {
            string valor = "";
            if(radioButton1.Checked == true)
            {
                return "Varon";
            }
            if (radioButton2.Checked == true)
            {
                return "Mujer";
            }
            if (radioButton3.Checked == true)
            {
                return "Otro";
            }
            return valor;
        }
        private void mostrarItems()
        {

            dataGridView1.Rows.Clear();

            foreach (Estudiante i in listaAlumnos)
            {
                string[] row = { "" + i.Codigo, i.Nombre, i.Edad, i.Celular, i.Email, i.Genero, i.FechaAdmision, i.Clase };
                dataGridView1.Rows.Add(row);
            }
        }
        public void Limpiar()
        {
            txtNombre.Text = "";
            txtEdad.Text = "";
            txtCelular.Text = "";
            txtEmail.Text = "";
            radioButton1.Checked = false;
            radioButton2.Checked = false;
            radioButton3.Checked = false;
        }
        private void btnEliminar_Click(object sender, EventArgs e)
        {
                        
            try
            {
                int n = dataGridView1.CurrentCell.RowIndex;               
                int contador = 0;

                foreach (Estudiante elem in listaAlumnos)
                {
                    if (contador == n)
                    {
                        listaAlumnos.Remove(elem);
                        break;
                    }
                    contador++;
                }

                mostrarItems();
            }
            catch (Exception eg)
            {
                MessageBox.Show("Seleccione un item de la tabla","ERROR");
            }
        }
    }
}
