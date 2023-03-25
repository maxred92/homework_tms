from aiohttp import web

routes = web.RouteTableDef()


async def handle(request):
    calculation = request.match_info.get('calculation', "Anonymous")
    try:
        if calculation.upper() in ['Q', 'QUIT']:
            print('Closing connection, bye-bye')
        else:
            result = eval(calculation)
    except (ZeroDivisionError):
        result = print("You can't divide by 0, try again")
    except (ArithmeticError):
        result = print('There is an error with your math, try again')
    except (SyntaxError):
        result = print('There is a syntax error, please try again')
    except (NameError):
        result = print('You did not enter an equation, try again')
        print(result)
        return web.Response(text=str(result))


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{calculation}', handle)])

if __name__ == '__main__':
    web.run_app(app)