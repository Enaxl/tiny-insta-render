from google.cloud import datastore

def delete_all():
    client = datastore.Client()
    for kind in ['Post', 'User']:
        print(f"Suppression des entités de type {kind}...")
        query = client.query(kind=kind)
        query.keys_only()
        
        while True:
            # On récupère les clés par paquets de 500 (limite de batch)
            keys = list(entity.key for entity in query.fetch(limit=500))
            if not keys:
                break
            client.delete_multi(keys)
            print(f"  - 500 {kind} supprimés")
    print("Base de données nettoyée !")

if __name__ == '__main__':
    delete_all()
