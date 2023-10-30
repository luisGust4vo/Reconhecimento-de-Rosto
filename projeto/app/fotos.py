import face_recognition as fr
from app.engine import reconhece_face, get_rostos
import face_recognition_models


desconhecido = reconhece_face("./img/imgl.jpg") #Fiz um teste de reconhecimento de imagem, para que o video reconheca
if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if(resultado):
            print("Rosto do", nomes_dos_rostos[i], "foi reconhecido")

else:
    print("Nao foi encontrado nenhum rosto")