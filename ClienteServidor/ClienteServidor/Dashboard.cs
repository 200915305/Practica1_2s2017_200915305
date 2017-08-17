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
using Newtonsoft.Json;
using System.Web.Script.Serialization;

namespace ClienteServidor
{
    public partial class Dashboard : Form
    {
        public String JSON = "";
        public String IP = "";
        public static String IPlocal = "127.0.0.1";
        List<string> listaIP = new List<string>();

        public Dashboard()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listaIP.Clear();
            flowLayoutPanel1.Controls.Clear();
            flowLayoutPanel2.Controls.Clear();
            flowLayoutPanel3.Controls.Clear();

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Archivos xml|*.xml|Archivos json|*.json";
            //ofd.FileName = "Seleccione un archivo de texto";
            ofd.Title = "Abrir...";

            string ruta = "";
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                ruta = ofd.FileName;
              

                System.IO.StreamReader sr = new System.IO.StreamReader(ruta, System.Text.Encoding.Default);
                string texto;
                texto = sr.ReadToEnd();
                sr.Close();

                JSON = texto;
                MessageBox.Show(JSON);
                MandarJSON(JSON);
                // MessageBox.Show("JSON enviado...");
            }

       
          try
            {
            F Friends = new System.Web.Script.Serialization.JavaScriptSerializer().Deserialize<F>(JSON);




            Console.WriteLine("local: {0}", Friends.nodos.local);
            IPlocal = Friends.nodos.local;
            Console.WriteLine("mascara: {0}", Friends.nodos.mascara);
            int i = 0;
            foreach (var item in Friends.nodos.nodo)
            {
                
                flowLayoutPanel1.ResetText();
                flowLayoutPanel2.ResetText();
                flowLayoutPanel3.ResetText();
                Console.WriteLine("ip: {0}, mascara: {1}", item.ip, item.mascara);
                /// Crear Botones..............
                /// 
                Label label1 = new Label();
                label1.Text = "Nodo"+i;
                label1.Size = new System.Drawing.Size(80, 50);
                flowLayoutPanel1.Controls.Add(label1);

                Label label2 = new Label();
                label2.Text = item.ip;
                listaIP.Add(item.ip);
                label2.Size = new System.Drawing.Size(80, 50);
                flowLayoutPanel2.Controls.Add(label2);

                Button bonton = new Button();
                bonton.Text = "ON/OFF";
                bonton.Name = Convert.ToString(i);
                bonton.Size = new System.Drawing.Size(80, 45);
                bonton.BackColor = Color.Silver; 
                flowLayoutPanel3.Controls.Add(bonton);
                bonton.Click += new EventHandler(LLamarGet);
                i++;
            }

            }
          catch
          {
              MessageBox.Show("Error con la Estructura del JSON");
          }


        }

        public void MandarJSON(string JSON) {
            try
            {
            // Create a request using a URL that can receive a post. 
                WebRequest request = WebRequest.Create("http://127.0.0.1:5000/" + "JSON");
            // Set the Method property of the request to POST.
            request.Method = "POST";
            // Create POST data and convert it to a byte array.
            string postData = "dato=" + JSON;
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
       

          /*
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
                Console.WriteLine("ip local..."+responseFromServer);
                // Clean up the streams.
                reader.Close();
                dataStream.Close();
                response.Close();
           * */
  
            }catch {
                MessageBox.Show("Se Cambio la IP del Servidor o error en el JSON");
            }
        
        
        }

        public void AgregarCarne(String carne) {
            try
            {
                // Create a request using a URL that can receive a post. 
                WebRequest request = WebRequest.Create("http://"+IPlocal+":5000/" + "carne");
                // Set the Method property of the request to POST.
                request.Method = "POST";
                // Create POST data and convert it to a byte array.
                string postData = "carne=" + carne;
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


            }
            catch
            {
                MessageBox.Show("Error al Agregar el Carne");
            }
        }

        
        public void LLamarGet(object sender, EventArgs e)
        {
            int b = 0;
            Button btn = sender as Button;
            Console.WriteLine("----------------------------------"+Convert.ToInt16(btn.Name));
            String ip = listaIP[Convert.ToInt16(btn.Name)];
            int a = MetodoGet(b,ip);
            if(a==0){
                btn.BackColor = Color.Silver;
            }else{
                btn.BackColor = Color.GreenYellow;
            }
        
            MessageBox.Show("IP " + listaIP[Convert.ToInt16(btn.Name)] );



        }

        private void button2_Click(object sender, EventArgs e)
        {   //Boton Regresar.........
            Form1 form = new Form1();
            this.Hide();
            form.ShowDialog();
            this.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            IPlocal = "127.0.0.1";

        }

        public int entero(int a) {

            return a;
        }

        public int MetodoGet(int a, String ip) { 
        //Metodo Get................
            try
            {
                string sURL;
                sURL = "http://"+ ip +":5000/" + "conectado";  /// ip es la direccion IP del Nodo...
                WebRequest wrGETURL;
                wrGETURL = WebRequest.Create(sURL);
                Stream objStream;
                objStream = wrGETURL.GetResponse().GetResponseStream();
                StreamReader objReader = new StreamReader(objStream);

                string sLine = "";
                int i = 0;

                while (sLine != null)
                {
                    i++;
                    sLine = objReader.ReadLine();
                    if (sLine != null)
                    {
                        Console.WriteLine("{0}:{1}", i, sLine);
                        MessageBox.Show(sLine);
                        AgregarCarne(ip+ "*" +sLine);  /// sLine es el Carne que devuelve el Nodo...
                        return 1;


                    }

                }
                Console.ReadLine();
                return 1;
               
            }
            catch{
                MessageBox.Show("No se Conecto <GET>");
                return 0;

              
            }


        }
        
        
        }





    }



    public class F {
        
        public Friends nodos { get; set; }
    }

    public class Friends
    {
       
        public string local { get; set; }
        public string mascara { get; set; }
        public List<FacebookFriend> nodo { get; set; }
    }

    public class FacebookFriend
    {

        //  public string carne { get; set; }
        public string ip { get; set; }
        public string mascara { get; set; }
    }
   


