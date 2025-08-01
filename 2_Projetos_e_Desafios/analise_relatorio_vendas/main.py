import pandas as pd
#importar a base de dados 
tabela_vendas = pd.read_excel('Vendas.xlsx')
#visualizar  a base de dados
pd.set_option('display.max_columns',None)
#faturamento po loja 
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
#quantidade de producto vendidos por loja
pordutos_por_loja = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
# tiket médio producto em cada loja
ticket_medio = (faturamento['Valor Final'] / pordutos_por_loja['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:'Ticket Médio'})

#enviar um email com o relatório
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = 'testes.testes@gmail.com.br'
mail.Subject = 'Relatorio de Vendas por Loja'
mail.HTMLBody = f''' 
<p>Prezados ,</P>

<p>Segue o Relatòtiro de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format })}


<p>Quantidade Vendida:</p>
{pordutos_por_loja.to_html()}


<p>ticket Médio dos productos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio':'R${:.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att,.</p>
<P>villarroel</P>
'''
mail.Send()
print('email enviado')

print(ticket_medio)
