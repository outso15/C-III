using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ciencias3
{

public partial class Login : Form{
 
       MySqlConnection con = new MySqlConnection("Server=''; Database=''; Uid=''; Pwd='';");
       public Login()
       {
            InitializeComponent();
        }
      
      
        private void Mysqlconnection(object sender, EventArgs e)
        {

        }
        private void Button1_click(object sender, EventArgs e)
        {
 
            try
            {
                con.Open();
                MessageBox.Show("Conectados");
                con.Close();
            }
            catch (Exception)
            {

                MessageBox.Show("Error");
            }

   
        }
        private void Label1_click(object sender, EventArgs e)
        {

        }
        private void Label3_click(object sender, EventArgs e)
        {

        }
        private void Loginb_click(object sender, EventArgs e)
        {
              String sql = sqldato.Text;
              MySqlCommand com = new MySqlCommand(sql, con);
              MySqlDataAdapter adp = new MySqlDataAdapter();
              adp.SelectCommand = com;
              DataTable tab = new DataTable();
              adp.Fill(tab);
              usuariosT.DataSource = tab;
			  int contador;
   
        }
        private void Sqldato_textchanged(object sender, EventArgs e)
        {

        }
        private void Login_load(object sender, EventArgs e)
        {

        }
}
}