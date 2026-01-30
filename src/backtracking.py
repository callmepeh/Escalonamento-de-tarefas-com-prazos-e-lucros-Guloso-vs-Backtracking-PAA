def job_sequencing(jobs, t):
    #ordenar todos os jobs em ordem decrescente de lucro
    jobs.sort(key=lambda x: x[2], reverse=True)

    #Criar um array para os slots de tempo (agenda)
    # Inicializamos tudo como vazio
    result = [None] * t
    slot = [False] * t

    lucro_total = 0

    for i in range(len(jobs)):
        #tentar encaixar o job do seu deadline máximo para trás
        for j in range(min(t, jobs[i][1]) - 1, -1, -1):
            
            #se o slot estiver livre, aloca o job
            if slot[j] is False:
                slot[j] = True
                result[j] = jobs[i][0]
                lucro_total += jobs[i][2]
                break

    return result, lucro_total


if __name__ == "__main__":
    job_sequencing()

