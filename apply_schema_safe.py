import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect('postgresql://fiscalis_cpy2_user:6ydNSQJdAA4gr4loD7tQ0aNWSIJ1td91@dpg-date1ohsrm7s738berhg-a.ohio-postgres.render.com/fiscalis_cpy2')
    with open('schema_actual.sql', 'r', encoding='utf-8') as f:
        sql = f.read()
    
    lines = [line for line in sql.split('\n') if not line.strip().startswith('\\')]
    sql_clean = '\n'.join(lines)
    
    statements = sql_clean.split(';')
    for stmt in statements:
        if not stmt.strip(): continue
        if 'OWNER TO' in stmt or 'SET ' in stmt or 'search_path' in stmt:
            continue
        try:
            await conn.execute(stmt)
        except Exception as e:
            if 'already exists' not in str(e):
                print(f'Ignorado: {stmt[:30].strip()}... -> {e}')
                
    print('Schema implementado de forma segura.')
    await conn.close()

asyncio.run(main())
