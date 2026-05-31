## Infraestrutura da Rede

As aplicacoes foram configuradas de forma estatica para operar no seguinte cenario de topologia na AWS:

| Instancia | IP Publico / IP de Rede | Papel no Ecossistema | Portas Utilizadas |
| :--- | :--- | :--- | :--- |
| **Servidor Central** | 3.227.138.6 | Concentrador de Binds / Processamento Intermediario | 5678, 5679 |
| **Peer 1** | 98.93.87.63 | Cliente / Consumidor Final / Assinante 1 | Conecta no Server |
| **Peer 2** | 44.220.64.119 | Produtor / Assinante 2 | Conecta no Server |

---

## Descricao dos Modulos e Funcionalidades Matematicas

### 1. Cliente-Servidor (/client-server)
Modelo classico Request-Reply de bloqueio sincrono transformado em uma Calculadora de Potencias Remota.
* **Nova Funcionalidade:** O cliente submete um valor base numerico de teste. O servidor calcula de forma distribuida o quadrado, o cubo e a raiz quadrada do numero, devolvendo um payload estruturado.
* **Porta:** 5678

### 2. Produtor-Consumidor em Pipeline (/pipeline_producer-consumer)
Arquitetura de distribuicao de tarefas paralela dividida em 3 estagios independentes, resolvendo a funcao matematica em cadeia: 
$$f(x) = (x \times 3) + 7$$

* **Estagio 1 - Produtor (producer.py no Peer 2):** Injeta valores numericos aleatorios ($x$) no pipeline.
* **Estagio 2 - Intermediario (worker_intermediate.py no Server):** Consome $x$ via socket PULL, realiza o calculo de multiplicacao ($y = x \times 3$) e retransmite o resultado adiante via socket PUSH.
* **Estagio 3 - Consumidor Final (consumer_final.py no Peer 1):** Consome $y$ via socket PULL, realiza a operacao final de soma ($z = y + 7$) e exibe metricas de desempenho.

### 3. Publish-Subscribe (/pub-sub)
Modelo assincrono de difusao de dados baseado em Filtros por Propriedades Numericas.
* **Nova Funcionalidade:** O publicador gera numeros aleatorios continuamente e classifica a propriedade do numero publicando sob os topicos estruturados PAR ou IMPAR.
* **Assinante 1 (sub_even.py no Peer 1):** Inscreve-se apenas no topico PAR e computa o somatorio acumulado na memoria.
* **Assinante 2 (sub_odd.py no Peer 2):** Inscreve-se apenas no topico IMPAR e computa a contagem de ocorrencias identificadas.

---

## Como Executar as Aplicacoes

Para testar os cenarios, acesse suas instancias via SSH, navegue ate a pasta do respectivo padrao e execute os comandos respeitando a ordem descrita abaixo para evitar falhas na descoberta de rota.

### Executando Cliente-Servidor
1. No Servidor (3.227.138.6):
   python3 client-server/server.py

2. No Peer 1 ou Peer 2:
   python3 client-server/client.py

### Executando o Pipeline de 3 Processos (Produtor-Consumidor)
1. No Servidor (3.227.138.6) - Inicializa o no central do pipeline:
   python3 pipeline_producer-consumer/worker_intermediate.py

2. No Peer 1 (3.235.239.109) - Inicializa o consumidor final:
   python3 pipeline_producer-consumer/consumer_final.py

3. No Peer 2 (100.52.205.229) - Inicializa a geracao de carga:
   python3 pipeline_producer-consumer/producer.py

### Executando o Publish-Subscribe
1. No Peer 1 (3.235.239.109) - Ativa a escuta de Pares:
   python3 pub-sub/sub_even.py

2. No Peer 2 (100.52.205.229) - Ativa a escuta de Impares:
   python3 pub-sub/sub_odd.py

3. No Servidor (3.227.138.6) - Inicia a transmissao de dados:
   python3 pub-sub/publisher.py

