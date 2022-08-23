import csv
import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def pagina_contagem(request):

    template_name = "upload-file.html"
    context = {}
    if "GET" == request.method:
	    return render (request, template_name, context)

    if "POST" == request.method:
        try:
            csv_file = request.FILES["csv_file"]
            response = HttpResponse(
                content_type='text/csv',
                # headers={'Content-Disposition': 'attachment; filename="UAAR.csv"'},
            )
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return HttpResponseRedirect(reverse("pagina-contagem"))
            # if file is too large, return
            if csv_file.multiple_chunks():
                messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                return HttpResponseRedirect(reverse("pagina-contagem"))

            file_data = csv_file.read().decode("utf-8")
            # writer = csv.writer(response)
            # writer.writerow(['name', 'loja', 'client_name', 'client_email', 'date',  'is_ok'])
            lines = file_data.split("\n")

            df = pd.DataFrame(columns=['produto', 'qtd', 'total'])

            count = 0
            qtd_arroz_b = 0
            qtd_acucar_a = 0
            qtd_acucar_b = 0
            qtd_macarrao_b = 0
            qtd_macarrao_a= 0
            qtd_arroz_a = 0
            qtd_sabonete_a = 0
            qtd_sabonete_b = 0
            qtd_pasta_de_dente_a = 0
            qtd_pasta_de_dente_b = 0
            qtd_alface = 0
            qtd_leite_a = 0
            qtd_leite_b = 0
            qtd_feijao_a = 0
            qtd_feijao_b = 0
            qtd_cerveja_a = 0
            qtd_cerveja_b = 0
            qtd_maionese_a = 0
            qtd_maionese_b = 0
            qtd_refrigerante = 0

            preco_arroz_b = 0
            preco_acucar_a = 0
            preco_acucar_b = 0
            preco_macarrao_b = 0
            preco_macarrao_a = 0
            preco_arroz_a = 0
            preco_sabonete_a = 0
            preco_sabonete_b = 0
            preco_pasta_de_dente_a = 0
            preco_pasta_de_dente_b = 0
            preco_alface = 0
            preco_leite_a = 0
            preco_leite_b = 0
            preco_feijao_a = 0
            preco_feijao_b = 0
            preco_cerveja_a = 0
            preco_cerveja_b = 0
            preco_maionese_a = 0
            preco_maionese_b = 0
            preco_refrigerante = 0


            for line in lines:
                fields = line.split(",")
                if not fields[0]=='':
                    produto = fields[0]
                    genero = fields[1]
                    preco = fields[2]


                    if produto == 'ARROZ B 5KG':
                        qtd_arroz_b = qtd_arroz_b+1
                        preco_arroz_b = preco_arroz_b + float(preco)

                    elif produto == 'ARROZ A 5KG':
                        qtd_arroz_a = qtd_arroz_a+1
                        preco_arroz_a = preco_arroz_a + float(preco)

                    elif produto == 'ACUCAR A 5KG':
                        qtd_acucar_a = qtd_acucar_a+1
                        preco_acucar_a = preco_acucar_a + float(preco)

                    elif produto == 'ACUCAR B 5KG':
                        qtd_acucar_b = qtd_acucar_b+1
                        preco_acucar_b = preco_acucar_b + float(preco)

                    elif produto == 'MACARRAO A 1KG':
                        qtd_macarrao_a = qtd_macarrao_a+1
                        preco_macarrao_a = preco_macarrao_a + float(preco)

                    elif produto == 'MACARRAO B 1KG':
                        qtd_macarrao_b = qtd_macarrao_b+1
                        preco_macarrao_b = preco_macarrao_b + float(preco)

                    elif produto == 'SABONETE A':
                        qtd_sabonete_a = qtd_sabonete_a+1
                        preco_sabonete_a = preco_sabonete_a + float(preco)

                    elif produto == 'SABONETE B 5KG':
                        qtd_sabonete_b = qtd_sabonete_b+1
                        preco_sabonete_b = preco_sabonete_b + float(preco)

                    elif produto == 'PASTA DE DENTE A':
                        qtd_pasta_de_dente_a = qtd_pasta_de_dente_a+1
                        preco_pasta_de_dente_a = preco_pasta_de_dente_a + float(preco)

                    elif produto == 'PASTA DE DENTE B':
                        qtd_pasta_de_dente_b = qtd_pasta_de_dente_b+1
                        preco_pasta_de_dente_b = preco_pasta_de_dente_b + float(preco)

                    elif produto == 'ALFACE':
                        qtd_alface = qtd_alface+1
                        preco_alface = preco_alface + float(preco)

                    elif produto == 'LEITE A 1L':
                        qtd_leite_a = qtd_leite_a+1
                        preco_leite_a = preco_leite_a + float(preco)

                    elif produto == 'LEITE B 1L':
                        qtd_leite_b = qtd_leite_b+1
                        preco_leite_b = preco_leite_b + float(preco)

                    elif produto == 'FEIJAO A 1KG':
                        qtd_feijao_a = qtd_feijao_a+1
                        preco_feijao_a = preco_feijao_a + float(preco)

                    elif produto == 'FEIJAO B 1KG':
                        qtd_feijao_b = qtd_feijao_b+1
                        preco_feijao_b = preco_feijao_b + float(preco)

                    elif produto == 'CERVEJA A':
                        qtd_cerveja_a = qtd_cerveja_a+1
                        preco_cerveja_a = preco_cerveja_a + float(preco)

                    elif produto == 'CERVEJA B':
                        qtd_cerveja_b = qtd_cerveja_b+1
                        preco_cerveja_b = preco_cerveja_b + float(preco)

                    elif produto == 'MAIONESE A':
                        qtd_maionese_a = qtd_maionese_a+1
                        preco_maionese_a = preco_maionese_a + float(preco)

                    elif produto == 'MAIONESE B':
                        qtd_maionese_b = qtd_maionese_b+1
                        preco_maionese_b = preco_maionese_b + float(preco)

                    elif produto == 'REFRIGERANTE':
                        qtd_refrigerante = qtd_refrigerante+1
                        preco_refrigerante = preco_refrigerante + float(preco)





            df = df.append([{'produto':'ARROZ_B_5KG','qtd' : qtd_arroz_b, 'total':preco_arroz_b}], ignore_index=True)
            df = df.append([{'produto':'ARROZ_A_5KG','qtd' : qtd_acucar_a, 'total':preco_acucar_a}], ignore_index=True)
            df = df.append([{'produto':'ACUCAR_A_5KG','qtd' : qtd_acucar_b, 'total':preco_acucar_b}], ignore_index=True)
            df = df.append([{'produto':'ACUCAR_B_5KG','qtd' : qtd_macarrao_b, 'total':preco_macarrao_b}], ignore_index=True)
            df = df.append([{'produto':'MACARRAO_A_1KG','qtd' : qtd_macarrao_a, 'total':preco_macarrao_a}], ignore_index=True)
            df = df.append([{'produto':'MACARRAO_B_1KG','qtd' : qtd_arroz_a, 'total':preco_arroz_a}], ignore_index=True)
            df = df.append([{'produto':'SABONETE_A','qtd' : qtd_sabonete_a, 'total':preco_sabonete_a}], ignore_index=True)
            df = df.append([{'produto':'SABONETE_B_5KG','qtd' : qtd_sabonete_b, 'total':preco_sabonete_b}], ignore_index=True)
            df = df.append([{'produto':'PASTA_DE_DENTE_A','qtd' : qtd_pasta_de_dente_a, 'total':preco_pasta_de_dente_a}], ignore_index=True)
            df = df.append([{'produto':'PASTA_DE_DENTE_B','qtd' : qtd_pasta_de_dente_b, 'total':preco_pasta_de_dente_b}], ignore_index=True)
            df = df.append([{'produto':'ALFACE','qtd' : qtd_alface, 'total':preco_alface}], ignore_index=True)
            df = df.append([{'produto':'LEITE_A_1L','qtd' : qtd_leite_a, 'total':preco_leite_a}], ignore_index=True)
            df = df.append([{'produto':'LEITE_B_1L','qtd' : qtd_leite_b, 'total':preco_leite_b}], ignore_index=True)
            df = df.append([{'produto':'FEIJAO_A 1KG','qtd' : qtd_feijao_a, 'total':preco_feijao_a}], ignore_index=True)
            df = df.append([{'produto':'FEIJAO_B 1KG','qtd' : qtd_feijao_b, 'total':preco_feijao_b}], ignore_index=True)
            df = df.append([{'produto':'CERVEJA_A','qtd' : qtd_cerveja_a, 'total':preco_cerveja_a}], ignore_index=True)
            df = df.append([{'produto':'CERVEJA_B','qtd' : qtd_cerveja_b, 'total':preco_cerveja_b}], ignore_index=True)
            df = df.append([{'produto':'MAIONESE_A','qtd' : qtd_maionese_a, 'total':preco_maionese_a}], ignore_index=True)
            df = df.append([{'produto':'MAIONESE_B','qtd' : qtd_maionese_b, 'total':preco_maionese_b}], ignore_index=True)
            df = df.append([{'produto':'REFRIGERANTE','qtd' : qtd_refrigerante, 'total':preco_refrigerante}], ignore_index=True)


            kmeans = KMeans(n_clusters=3, random_state=0)
            df['cluster'] = kmeans.fit_predict(df[['total', 'qtd']])

            centroids = kmeans.cluster_centers_
            cen_x = [i[0] for i in centroids]
            cen_y = [i[1] for i in centroids]
            ## add to df
            df['cen_x'] = df.cluster.map({0: cen_x[0], 1: cen_x[1], 2: cen_x[2]})
            df['cen_y'] = df.cluster.map({0: cen_y[0], 1: cen_y[1], 2: cen_y[2]})  # define and map colors
            colors = ['#DF2020', '#81DF20', '#2095DF']
            df['c'] = df.cluster.map({0: colors[0], 1: colors[1], 2: colors[2]})


            plt.scatter(df.qtd, df.total, c=df.c, alpha=0.6, s=10)
            plt.savefig('output.jpg')
            object = df.to_html(classes='data', header="true")
            context = {'objects': object}
            return render(request,'registration/upload-file.html', context)

        except Exception as e:
            print(e)
            messages.error(request, str(e))
            return HttpResponseRedirect(reverse("pagina-contagem"))


def write(request):
    import random
    response = HttpResponse(
        content_type='text/csv',
        # headers={'Content-Disposition': 'attachment; filename="UAAR.csv"'},
    )

    filename = "records.csv"

    # writing to csv file


    writer = csv.writer(response)
    writer.writerow(['produto', 'genero', 'preco'])

    for x in range(10000):
        rd = random.randint(1, 20)

        if rd == 1:
            produto = 'ARROZ B 5KG'
            genero = 'ALIMENTICIO'
            preco = 5
        elif rd == 2:
            produto = 'ARROZ A 5KG'
            genero = 'ALIMENTICIO'
            preco = 7
        elif rd == 3:
            produto = 'ACUCAR A 5KG'
            genero = 'ALIMENTICIO'
            preco = 8
        elif rd == 4:
            produto = 'ACUCAR B 5KG'
            genero = 'ALIMENTICIO'
            preco = 12
        elif rd == 5:
            produto = 'MACARRAO A 1KG'
            genero = 'ALIMENTICIO'
            preco = 4
        elif rd == 6:
            produto = 'MACARRAO B 1KG'
            genero = 'ALIMENTICIO'
            preco = 6
        elif rd == 7:
            produto = 'SABONETE A'
            genero = 'HIGIENE'
            preco = 1
        elif rd == 8:
            produto = 'SABONETE B 5KG'
            genero = 'HIGIENE'
            preco = 2
        elif rd == 9:
            produto = 'PASTA DE DENTE A'
            genero = 'HIGIENE'
            preco = 7
        elif rd == 10:
            produto = 'PASTA DE DENTE B'
            genero = 'HIGIENE'
            preco = 9
        elif rd == 11:
            produto = 'ALFACE'
            genero = 'HORTIFRUTI'
            preco = 3
        elif rd == 12:
            produto = 'LEITE A 1L'
            genero = 'LATICINIO'
            preco = 9
        elif rd == 13:
            produto = 'LEITE B 1L'
            genero = 'LATICINIO'
            preco = 7
        elif rd == 14:
            produto = 'FEIJAO A 1KG'
            genero = 'ALIMENTICIO'
            preco = 15
        elif rd == 15:
            produto = 'FEIJAO B 1KG'
            genero = 'ALIMENTICIO'
            preco = 20
        elif rd == 16:
            produto = 'CERVEJA A'
            genero = 'BEBIDAS'
            preco = 5
        elif rd == 17:
            produto = 'CERVEJA B'
            genero = 'BEBIDAS'
            preco = 9
        elif rd == 18:
            produto = 'MAIONESE A'
            genero = 'ALIMENTICIO'
            preco = 1
        elif rd == 19:
            produto = 'MAIONESE B'
            genero = 'ALIMENTICIO'
            preco = 2
        elif rd == 20:
            produto = 'REFRIGERANTE'
            genero = 'ALIMENTICIO'
            preco = 10

        writer.writerow([produto, genero, preco])

    return response