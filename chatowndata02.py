import os
from langchain_fireworks import ChatFireworks # type: ignore
from langchain_community.document_loaders import TextLoader # type: ignore
from langchain_fireworks import FireworksEmbeddings # type: ignore
from langchain.indexes import VectorstoreIndexCreator # type: ignore

key = "dTrpGZ6nUsf3WAbMCsOdUDrXro2LRndwlUd1AEvGneQEdjiO"
os.environ["FIREWORKS_API_KEY"] = key
llm = ChatFireworks(model = "accounts/fireworks/models/mixtral-8x7b-instruct")

def Predecir():
    query = "Dime cual es el resultado mas probable local, empate o visita. Si el equipo A es local y el equipo B visita, ambos pertenecen a la Liga X, una respuesta concreta."
    #print(query)
    loader = TextLoader('data_.txt')
    index = VectorstoreIndexCreator(embedding=FireworksEmbeddings()).from_loaders([loader])
    response = index.query(query,llm)
    print(response)
    return response


