using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ClienteServidor
{
    public partial class Respuestas_de_Mensajes : Form
    {
        public Respuestas_de_Mensajes()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Mensajes mensajes = new Mensajes();
            this.Hide();
            mensajes.ShowDialog();
            this.Close();
        }
    }
}
