import json_manager
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='Name of user')
@click.option('--lastname', required=True, help='Lastname of user')
@click.pass_context  # Este lo que nos permite es mostrar un error por consola
def new_user(contexto, name, lastname):
    if not name or not lastname:
        contexto.fail('the name and lastname are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        user = {'id': new_id, 'name': name, 'lastname': lastname}
        # Despues de crear el user lo que hago es empujarlo a la lista para que cuando llame a la funcion de escritura en json_manager tenga el arreglo completo
        data.append(user)
        json_manager.write_json(data)
        print(f"User {name} {lastname} created successfully with id {new_id}")


@cli.command()
def users():
    # Ahora leeo los datos con la funcion que creee en json_manager
    users = json_manager.read_json()
    for user in users:
        message = f"{user['id']} - {user['name']} - {user['lastname']}"
        print(message)


@cli.command()
@click.argument("id")
def user(id):
    users = json_manager.read_json()

    # Aca estoy diciendo que me devuelva el elemento entero  y el resultante de la condicion que si el
    # id es igual al parametro devolvemelo sino, no se devuelve
    user_by_id = next((user for user in users if user["id"] == int(id)), None)
    if user_by_id is None:
        print(f"The user with id {id} doesn't exist")
    else:
        print(f""" -ID: {id}             
 -Nombre: {user_by_id["name"]}
 -Lastname: {user_by_id["lastname"]}""")


@cli.command()
@click.argument("id", type=int)
def delete_user(id):
    users = json_manager.read_json()
    user_by_id = next((user for user in users if user["id"] == id), None)
    if user_by_id is None:
        print(f"The user with id {id} doesn't exist")
    else:
        users.remove(user_by_id)
        json_manager.write_json(users)
        print(f"The user with id {id} does delete successfully")


@cli.command()
@click.argument("id", type=int)
@click.option('--name', help='Name of the user', default=None)
@click.option('--lastname', help='Lastname of the user', default=None)
def update_user(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] is not id:
            print(f"The user {id} doesn't exist")
            break
        else:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break
    print(f"The user {id} was udapted")
    json_manager.write_json(data)


if __name__ == '__main__':
    cli()
