using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Net;
using System.Collections.Specialized;
using System.Xml.Linq;
using Newtonsoft.Json;
using System.Web.Script.Serialization;





namespace ClienteServidor
{       
   

     public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            Dashboard dash = new Dashboard();
            this.Hide();
            dash.ShowDialog();
            this.Close();
 
       
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Mensajes mensajes = new Mensajes();
            this.Hide();
            mensajes.ShowDialog();
            this.Close();
            

               
          
        }




    }

     

 
}
