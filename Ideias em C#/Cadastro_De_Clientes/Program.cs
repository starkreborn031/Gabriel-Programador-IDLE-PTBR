using System;
using System.IO;
using iTextSharp.text;
using iTextSharp.text.pdf;
using ConsoleTables;

namespace CadastroClientes
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Cadastro de Clientes e Computadores\n");

            // Solicitar informações do cliente
            Console.Write("Nome completo do cliente: ");
            string nome = Console.ReadLine();

            Console.Write("CPF do cliente: ");
            string cpf = Console.ReadLine();

            Console.Write("Data de nascimento do cliente (DD/MM/AAAA): ");
            string dataNascimento = Console.ReadLine();

            Console.Write("Endereço do cliente: ");
            string endereco = Console.ReadLine();

            // Solicitar informações do computador
            Console.WriteLine("\nCadastro do computador:");
            Console.Write("Tipo de computador (Desktop/Notebook/PC Gamer): ");
            string tipoComputador = Console.ReadLine();

            Console.Write("Modelo do computador: ");
            string modeloComputador = Console.ReadLine();

            Console.Write("Valor do computador: ");
            double valorComputador = double.Parse(Console.ReadLine());

            Console.Write("Desconto (%): ");
            double desconto = double.Parse(Console.ReadLine());

            Console.Write("Observações: ");
            string observacoes = Console.ReadLine();

            // Gerar número de registro único
            string numeroRegistro = Guid.NewGuid().ToString();

            // Gerar PDF
            string nomeArquivo = $"Cadastro_Cliente_{numeroRegistro}.pdf";
            Document doc = new Document();
            PdfWriter.GetInstance(doc, new FileStream(nomeArquivo, FileMode.Create));
            doc.Open();

            // Cabeçalho
            Paragraph cabecalho = new Paragraph("STARK TECH MG\n\n");
            cabecalho.Alignment = Element.ALIGN_CENTER;
            doc.Add(cabecalho);

            // Tabela com informações do cliente e computador
            ConsoleTable table = new ConsoleTable("Informação", "Valor");
            table.AddRow("Número de registro", numeroRegistro);
            table.AddRow("Nome completo", nome);
            table.AddRow("CPF", cpf);
            table.AddRow("Data de nascimento", dataNascimento);
            table.AddRow("Endereço", endereco);
            table.AddRow("Tipo de computador", tipoComputador);
            table.AddRow("Modelo do computador", modeloComputador);
            table.AddRow("Valor do computador", $"R$ {valorComputador:F2}");
            table.AddRow("Desconto", $"{desconto}%");
            table.AddRow("Observações", observacoes);
            doc.Add(new Paragraph(table.ToString()));

            // Data e hora
            Paragraph dataHora = new Paragraph($"\nData e hora: {DateTime.Now}\n\n");
            dataHora.Alignment = Element.ALIGN_RIGHT;
            doc.Add(dataHora);

            // Assinatura
            Paragraph assinatura = new Paragraph("Assinatura: ____________________\n");
            assinatura.Alignment = Element.ALIGN_CENTER;
            doc.Add(assinatura);

            doc.Close();

            Console.WriteLine($"\nPDF gerado com sucesso: {nomeArquivo}");
        }
    }
}
