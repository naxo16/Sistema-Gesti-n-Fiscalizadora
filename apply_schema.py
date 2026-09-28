import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect('postgresql://fiscalis_cpy2_user:6ydNSQJdAA4gr4loD7tQ0aNWSIJ1td91@dpg-date1ohsrm7s738berhg-a.ohio-postgres.render.com/fiscalis_cpy2')
    with open('schema_actual.sql', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Quitar comandos especiales de psql (\restrict, \unrestrict, etc)
    cleaned_sql = "".join([line for line in lines if not line.strip().startswith('\\')])
    
    try:
        await conn.execute(cleaned_sql)
        print('Schema aplicado correctamente')
    except Exception as e:
        print(f'Error aplicando schema: {e}')
    finally:
        await conn.close()

asyncio.run(main())
