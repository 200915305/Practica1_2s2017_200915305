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

using System.Xml;
using System.Xml.XPath;
using System.Xml.Linq;

namespace ClienteServidor
{
    public partial class Enviar_Mensajes : Form
    {
       public String XML = "";
       public string ruta = "";

        public Enviar_Mensajes()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Mensajes mensajes = new Mensajes();
            this.Hide();
            mensajes.ShowDialog();
            this.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Archivos xml|*.xml|Archivos json|*.json";
            //ofd.FileName = "Seleccione un archivo de texto";
            ofd.Title = "Abrir...";

           
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                ruta = ofd.FileName;


                System.IO.StreamReader sr = new System.IO.StreamReader(ruta, System.Text.Encoding.Default);
                string texto;
                texto = sr.ReadToEnd();
                sr.Close();

                XML = texto;
                textBox1.Text = XML;
            }


              
            


      

        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            XML = "";
        }

        private void button2_Click(object sender, EventArgs e)
        {  
             try
            {
            List<string> ips = new List<string>();
            int i = 0;


            foreach (XElement level1Element in XElement.Load(ruta).Elements("mensaje"))
            {

                foreach (XElement level2Element in level1Element.Elements("nodos"))
                {

                    foreach (XElement level3Element in level2Element.Elements("IP"))
                    {
                        ips.Add(level3Element.Value);
                        Console.WriteLine(" <<<<<<< " + level3Element.Value);
                    }

                }

                foreach (XElement level4Element in level1Element.Elements("texto"))
                {

                    Console.WriteLine(" <<<<<<< " + level4Element.Value);


                    ips.ForEach(delegate(String name)
                    {
                        ///Mandar los Mensajes........................
                        EnviarMensaje(ips[i], level4Element.Value);
                       // MessageBox.Show("Texto" + level4Element.Value + "Nodo" + ips[i]);
                        i++;
                    });

                    i = 0;
                    ips.Clear();
                }


            }

            }
             catch
             {
                 MessageBox.Show("No se puede enviar el Mensaje");
             }

        }


        public void EnviarMensaje(String ip, String mensaje){

            mensaje = mensaje.Replace("+","#");
            ip = ip.Replace(" ", "");
            ip = ip.Replace("\n", "");
  
            try
            {
                // Create a request using a URL that can receive a post. 
                Console.WriteLine("http://" + ip + ":5000/");
                WebRequest request = WebRequest.Create("http://" + ip + ":5000/" + "mensaje");
 
                // Set the Method property of the request to POST.
                request.Method = "POST";
                // Create POST data and convert it to a byte array.
                string postData = "mensaje=" + mensaje;
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
                MessageBox.Show(responseFromServer);
                Console.WriteLine(responseFromServer);
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
    }
}
