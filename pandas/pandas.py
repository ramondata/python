# Biblioteca Pandas e numpy

# Estruturas de dados -------------------------------------------------------------------------------------------------------------------------------------------------
Series ndarray                                       -> var = pd.Series([dados], index=[índice de dados], name='nomeie a serie') #Constrói um vetor ou coluna Serie
Series dict                                          -> var = {'index1':dado1, 'index2':dado2, 'index3':dado3, ...} -> pd.Series(var) #Dar preferencia a Serie ndarray
Index                                                -> var.index #Verifica a estrutura da Serie construída
Explorar Serie                                       -> var[:xx ou var > xx ou var = median() 'apenas exemplos'] #Pega os 'xx' primeiros termos da Serie
var.dtype                                            -> #Descobrir tipo de dado da Serie, precisa ser usado em ndarray, não funciona e dict
Series var.array                                     -> #Verifica a estrutura da Serie construída no campo do dados
to_numpy                                             -> #Converte Serie tipo Pandas para tipo Numpy
var.rename('novo_nome')                              -> #Mudar o apelido dado a Serie
DataFrame(tabela)                                   -> var = {  'nome_coluna1': pd.Series([dados], index=[indices], name='apelido da coluna1' , 
                                                                'nome_coluna2': pd.Series([dados], index=[indices], name='apelido da coluna2' ,
                                                                'nome_coluna3': pd.Series([dados], index=[indices], name='apelido da coluna3' ,
                                                                'nome_colunaN': pd.Series([dados], index=[indices], name='apelido da colunaN'
                                                             }
pd.DataFrame(var, index=[], columns=[])              -> #Explora um dataframe com indices desejados e colunas desejadas
var.columns                                          -> #Tras as colunas de um dataframe
head()                                               -> #var.head(xx), tras as primeiras linhas da tabela
.tail()                                              -> #Retorna as ultimas linhas da tabela
.sum(axis=0 - Index, axis=1 - Column)                -> #Soma os valores numéricos de uma coluna
.mean()                                              -> #Média dos valores de uma coluna
.median()                                            -> #Mediana dos valores de uma coluna
.value_counts()                                      -> #Contagem de linhas de uma coluna
.describe()                                          -> #Descreve as informações das colunas
var['nome da coluna']                                -> #Selecionar coluna
.drop()                                              -> #Eliminar uma coluna ou uma linha
var.insert(Qtd, 'nome da nova coluna', dados)        -> #Inserir nova coluna
var['nome da nova coluna'] = valor do domínio        -> #Outro modo de inserir uma coluna
del var['nome da coluna']                            -> #Deleta uma coluna
var.to_csv('nome para o novo arquivo.csv')           -> #Exporta um dataframe(object) do tratado no python para .csv
.to_string()
.any()
.empty
.bool()
.all()
var1.equals()var2
DataFrame.combine()
.std()
.apply()
