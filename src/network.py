import logging

from httpx import AsyncClient

logging.basicConfig(level=logging.DEBUG)


async def get_state():
    async with AsyncClient() as client:
        async with client.stream("GET", "http://localhost:10000/api/sse/") as response:
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    data = line[len("data:") :].strip()
                    logging.debug(f"Received data: {data}")
                    # Обработка данных по мере их поступления
                    data = data.strip("b'")

                    logging.info(data)

                    yield tuple(
                        float(value)
                        for value in data.split(",")
                    )
                    
                
