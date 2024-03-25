using System;
using System.IO;
using System.Windows.Forms;
using iTextSharp.text;
using iTextSharp.text.pdf;

namespace CadastroClientesWinForms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Implementação do método Dispose(bool)
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            // Inicialização dos componentes do formulário
            this.components = new System.ComponentModel.Container();
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Text = "Form1";
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Name = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private void btnGerarPDF_Click(object sender, EventArgs e)
        {
            // Capturar informações do formulário
            string nome = txtNome.Text;
            string cpf = txtCPF.Text;
            string dataNascimento = txtDataNascimento.Text;
            string endereco = txtEndereco.Text;
            string tipoComputador = txtTipoComputador.Text;
            string modeloComputador = txtModeloComputador.Text;
            double valorComputador = double.Parse(txtValorComputador.Text);
            double desconto = double.Parse(txtDesconto.Text);
            string observacoes = txtObservacoes.Text;
            string horaData = DateTime.Now.ToString("HH:mm dd/MM/yyyy");
            string assinatura = txtAssinatura.Text;
            string relatoProblema = txtRelatoProblema.Text;

            // Gerar número de registro único
            string numeroRegistro = Guid.NewGuid().ToString();

            // Gerar PDF
            string nomeArquivo = $"Cadastro_Cliente_{numeroRegistro}.pdf";
            Document doc = new Document();
            PdfWriter.GetInstance(doc, new FileStream(nomeArquivo, FileMode.Create));
            doc.Open();

            // Adicionar conteúdo ao PDF
            Paragraph conteudo = new Paragraph();
            conteudo.Add(new Paragraph("STARK TECH MG\n\n", new Font(Font.FontFamily.HELVETICA, 18, Font.BOLD)));
            conteudo.Add(new Paragraph($"Número de registro: {numeroRegistro}\n\n"));
            conteudo.Add(new Paragraph($"Nome completo: {nome}\n"));
            conteudo.Add(new Paragraph($"CPF: {cpf}\n"));
            conteudo.Add(new Paragraph($"Data de nascimento: {dataNascimento}\n"));
            conteudo.Add(new Paragraph($"Endereço: {endereco}\n\n"));
            conteudo.Add(new Paragraph($"Tipo de computador: {tipoComputador}\n"));
            conteudo.Add(new Paragraph($"Modelo do computador: {modeloComputador}\n"));
            conteudo.Add(new Paragraph($"Valor do computador: R$ {valorComputador:F2}\n"));
            conteudo.Add(new Paragraph($"Desconto: {desconto}%\n"));
            conteudo.Add(new Paragraph($"Observações: {observacoes}\n"));
            conteudo.Add(new Paragraph($"Hora e data: {horaData}\n"));
            conteudo.Add(new Paragraph($"Assinatura: {assinatura}\n\n"));
            conteudo.Add(new Paragraph($"Relato do problema: {relatoProblema}\n"));

            doc.Add(conteudo);
            doc.Close();

            MessageBox.Show($"PDF gerado com sucesso: {nomeArquivo}", "Sucesso", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
