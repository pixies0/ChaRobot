def entrada_unica_serializer(entrada) -> dict:
    return {
        "id": str(entrada["_id"]),
        "tipo": entrada["tipo"],
        "valor": entrada["valor"],
    }


def entrada_lista_serializer(entradas) -> dict:
    return [entrada_unica_serializer(entrada) for entrada in entradas]


def usuario_unico_serializer(usuario) -> dict:
    return {
        "id": str(usuario.get("_id")),
        "user_id": usuario.get("user_id"),
        "nome": usuario.get("nome"),
        "total_entradas": len(usuario.get("entradas", [])),
    }
