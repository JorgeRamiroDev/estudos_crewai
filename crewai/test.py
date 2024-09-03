# import os
# from crewai import Agent, Task, Crew, Process
# from crewai_tools import PDFSearchTool
# from langchain_openai import ChatOpenAI

# # Definindo uma classe de ferramenta personalizada para ler PDFs
# tool = PDFSearchTool()

# # Criando um agente leitor de PDF
# pdf_reader = Agent(
#     role="Leitor de PDF",
#     goal = "Ler e extrair texto de um Documento PDF",
#     verbose = True,
#     memory = False,
#     backstory = "Você é um profissional em ler pdf e extrair informações importantes",
#     llm = ChatOpenAI(model="gpt-4o-mini"),
# )

# # Configurando a tarefa para ler um PDF específico
# pdf_task = Task(
#   description="ler o conteudo do documento pdf e retornar no texto extraido",
#   expected_output="Em portugues um csv com informação das vendas por unidade",
#   tools= tool,  # Passando a classe PDFReaderTool diretamente
#   agent=pdf_reader,
# )

# # Configurando a crew para realizar a tarefa de leitura
# crew = Crew(
#   agents=[pdf_reader],
#   tasks=[pdf_task],
#   process=Process.sequential
# )

# # Executando a tarefa
# result = crew.kickoff(inputs={'file_path': 'dados\\CERTIDÃO RESIDENCIAL VITÓRIA - JANEIRO 2024.pdf'})
# print(result)

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI

# Definindo uma classe de ferramenta personalizada para ler PDFs
tool = PDFSearchTool()

# Criando um agente leitor de PDF
pdf_reader = Agent(
    role="Leitor de PDF",
    goal="Ler e extrair texto de um Documento PDF",
    verbose=True,
    memory=True,
    backstory="Você é um profissional em ler pdf e extrair informações importantes",
    llm=ChatOpenAI(model="gpt-4o-mini",verbose =True),
)

# Configurando a tarefa para ler um PDF específico
pdf_task = Task(
    
    description="Ler o conteúdo do documento PDF em {file_path} , pagina por pagina, e incrementar a cada pagina as informações",
    expected_output="Em português, um CSV com informação das vendas por unidade",
    tools=[tool],  # Passando a ferramenta como lista de dicionários
    agent=pdf_reader,
)

# Configurando a crew para realizar a tarefa de leitura
crew = Crew(
    agents=[pdf_reader],
    tasks=[pdf_task],
    process=Process.sequential
)

# Executando a tarefa
# Supondo que a description da tarefa tenha um placeholder chamado 'file_path'
result = crew.kickoff(inputs={'file_path': 'dados\\CERTIDÃO RESIDENCIAL VITÓRIA - JANEIRO 2024.pdf'})

print(result)
