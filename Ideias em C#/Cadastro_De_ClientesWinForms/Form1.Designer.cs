using System;
using System.Windows.Forms;
using System.Drawing; // Adicionando referência para System.Drawing

namespace Cadastro_De_ClientesWinForms
{
    public partial class Form1 : Form
    {
        private System.ComponentModel.IContainer components = null;
        private Label labelNome;
        private TextBox textBoxNome;
        private Label labelCPF;
        private TextBox textBoxCPF;
        private Label labelDataNascimento;
        private TextBox textBoxDataNascimento;
        private Label labelEndereco;
        private TextBox textBoxEndereco;
        private Button buttonSalvar;
        private Button buttonLimpar;

        public Form1()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.labelNome = new Label();
            this.labelCPF = new Label();
            this.labelDataNascimento = new Label();
            this.labelEndereco = new Label();
            this.textBoxNome = new TextBox();
            this.textBoxCPF = new TextBox();
            this.textBoxDataNascimento = new TextBox();
            this.textBoxEndereco = new TextBox();
            this.buttonSalvar = new Button();
            this.buttonLimpar = new Button();

            // Configuração dos componentes
            this.SuspendLayout();

            // labelNome
            this.labelNome.AutoSize = true;
            this.labelNome.Location = new System.Drawing.Point(50, 50);
            this.labelNome.Size = new System.Drawing.Size(100, 20);
            this.labelNome.Text = "Nome completo:";

            // labelCPF
            this.labelCPF.AutoSize = true;
            this.labelCPF.Location = new System.Drawing.Point(50, 100);
            this.labelCPF.Size = new System.Drawing.Size(100, 20);
            this.labelCPF.Text = "CPF:";

            // labelDataNascimento
            this.labelDataNascimento.AutoSize = true;
            this.labelDataNascimento.Location = new System.Drawing.Point(50, 150);
            this.labelDataNascimento.Size = new System.Drawing.Size(200, 20);
            this.labelDataNascimento.Text = "Data de nascimento (DD/MM/AAAA):";

            // labelEndereco
            this.labelEndereco.AutoSize = true;
            this.labelEndereco.Location = new System.Drawing.Point(50, 200);
            this.labelEndereco.Size = new System.Drawing.Size(100, 20);
            this.labelEndereco.Text = "Endereço:";

            // textBoxNome, textBoxCPF, textBoxDataNascimento, textBoxEndereco
            // Defina as propriedades Location e Size para os TextBoxes conforme necessário

            // buttonSalvar
            this.buttonSalvar.Location = new System.Drawing.Point(200, 300);
            this.buttonSalvar.Size = new System.Drawing.Size(100, 30);
            this.buttonSalvar.Text = "Salvar";
            this.buttonSalvar.Click += new EventHandler(buttonSalvar_Click);

            // buttonLimpar
            this.buttonLimpar.Location = new System.Drawing.Point(350, 300);
            this.buttonLimpar.Size = new System.Drawing.Size(100, 30);
            this.buttonLimpar.Text = "Limpar";
            this.buttonLimpar.Click += new EventHandler(buttonLimpar_Click);

            // Adicionando controles ao formulário
            this.Controls.Add(this.labelNome);
            this.Controls.Add(this.labelCPF);
            this.Controls.Add(this.labelDataNascimento);
            this.Controls.Add(this.labelEndereco);
            this.Controls.Add(this.textBoxNome);
            this.Controls.Add(this.textBoxCPF);
            this.Controls.Add(this.textBoxDataNascimento);
            this.Controls.Add(this.textBoxEndereco);
            this.Controls.Add(this.buttonSalvar);
            this.Controls.Add(this.buttonLimpar);

            this.Name = "Form1";
            this.Text = "Cadastro de Clientes";

            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private void buttonSalvar_Click(object sender, EventArgs e)
        {
            // Lógica para salvar os dados
        }

        private void buttonLimpar_Click(object sender, EventArgs e)
        {
            // Lógica para limpar os campos do formulário
        }
    }
}
