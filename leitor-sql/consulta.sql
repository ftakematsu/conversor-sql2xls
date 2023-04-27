SELECT 
	empregados.empresa AS codigo_da_empresa, 
	empregados.empresa AS codigo_do_estabelecimento, 
	empregados.idpessoa AS codigo_do_funcionario,
	empregados.nome AS nome,
	ifnull(empregados.sexo,"") AS sexo,
	ifnull(DATE_FORMAT(empregados.nascimento, '%d/%m/%Y'),"") AS data_nascimento,
	ifnull(empregados.cpf,"") AS cpf,
	ifnull(empregados.rg,"") AS rg,
	ifnull(empregados.ctps,"") AS ctps,
	ifnull(empregados.serie,"") AS serie,
	ifnull(empregados.ctps,"") AS n_inscricao,
	DATE_FORMAT(empregados.admissao, '%d/%m/%Y') AS admissao,
	ifnull(cargos.cargo,"") AS funcao,
	ifnull(setores.setor,"") AS posto_de_trabalho,
	"" AS cargo,
	ifnull(empregados.matricula,"") AS matricula_esocial
FROM empregados
LEFT JOIN empresas ON empregados.empresa=empresas.id
LEFT JOIN setores ON (empregados.idsetor=setores.id AND setores.empresa=empresas.id)
LEFT JOIN cargos ON (cargos.id=empregados.idcargo AND cargos.idsetor=setores.id AND cargos.idempresa=empresas.id)
INTO OUTFILE 'D:/files/backup-final.csv' 
FIELDS ENCLOSED BY '' 
TERMINATED BY ',' 
ESCAPED BY '' 
LINES TERMINATED BY '\r\n';