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

namespace ClienteServidor
{
    public partial class Cola_de_Mensajes : Form
    {
        public Cola_de_Mensajes()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Mensajes mensajes = new Mensajes();
            this.Hide();
            mensajes.ShowDialog();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {          //Boton Operar
            EnviarMensaje("","Operaciones");

        }

        public void EnviarMensaje(String ip, String mensaje)
        {

            String nuevaip = Dashboard.IPlocal;

            Console.WriteLine("http://" + nuevaip + ":5000/");
            try
            {
                // Create a request using a URL that can receive a post. 
                Console.WriteLine("http://" + nuevaip + ":5000/");
                WebRequest request = WebRequest.Create("http://"+nuevaip+":5000/" + "respuesta");
                // Set the Method property of the request to POST.
                request.Method = "POST";
                // Create POST data and convert it to a byte array.
                string postData = "respuesta=" + mensaje;
                byte[] byteArray = Encoding.UTF8.GetBytes(postData);
                // Set the ContentType property of the WebRequest.
                request.ContentType = "application/x-www-form-urlencoded";
                // Set the ContentLength property of the WebRequest.
                request.ContentLength = byteArray.Length;
                // Get the request stream.

                Stream dataStream = request.GetRequestStream();
                // Write the data to the request stream.
                dataStream.Write(byteArray, 0, byteArray.Length);
                // Close the Stream object.
                dataStream.Close();
                // Get the response.



                WebResponse response = request.GetResponse();
                // Display the status.
                Console.WriteLine(((HttpWebResponse)response).StatusDescription);
                // Get the stream containing content returned by the server.
                dataStream = response.GetResponseStream();
                // Open the stream using a StreamReader for easy access.
                StreamReader reader = new StreamReader(dataStream);
                // Read the content.
                string responseFromServer = reader.ReadToEnd();
                // Display the content.
                //MessageBox.Show(responseFromServer);
                Console.WriteLine(responseFromServer);
                string[] words = responseFromServer.Split(',');
                textBox1.Text = words[3];
                textBox2.Text = words[1];
                textBox3.Text = words[4];
                textBox4.Text = words[0];
                textBox5.Text = words[2];
                richTextBox1.Text = words[5];
                // Clean up the streams.
                reader.Close();
                dataStream.Close();
                response.Close();
            }
            catch
            {
                MessageBox.Show("ERROR al enviar el XML");
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
         
        }


    }
}
