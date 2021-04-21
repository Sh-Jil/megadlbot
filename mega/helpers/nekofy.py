import aiohttp


class Nekobin:
    def __init__(self):
        """ Interacts with the paste service Nekobin using its API.
        functions:
            nekofy: post a payload to nekobin.com using its API and return the link for saved paste page.
        """
        self.neko_endpoint = "https://nekobin.com/api/documents"

    async def nekofy(self, payload_content: str):
        async with aiohttp.ClientSession() as nekoSession:
            payload = {"content": payload_content}
            async with nekoSession.post(self.neko_endpoint, data=payload) as resp:
                neko_link = f"https://nekobin.com/{(await resp.json())['result']['key']}.py"
        return neko_link
