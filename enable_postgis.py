import asyncio
import asyncpg
import os

async def main():
    conn = await asyncpg.connect('postgresql://fiscalis_cpy2_user:6ydNSQJdAA4gr4loD7tQ0aNWSIJ1td91@dpg-date1ohsrm7s738berhg-a.ohio-postgres.render.com/fiscalis_cpy2')
    await conn.execute('CREATE EXTENSION IF NOT EXISTS postgis;')
    print('PostGIS enabled successfully!')
    await conn.close()

asyncio.run(main())
