import re
from mega.database import MegaDB
from bson.objectid import ObjectId


class MegaFiles:
    def __init__(self):
        """ MegaFiles is the mongo collection that holds the documents for the files that are uploaded via the bot.
        Functions:
            insert_new_files: save new documents to the collection that contains details of the new files that are
            uploaded.
            count_files_by_url: count and returns the number of documents for the file with the same url.
            get_files_by_url: returns the documents for the files with a given url.
            get_file_by_file_id: returns the document for the file with the given telegram file_id.
            get_file_by_file_name: returns the documents for the files with the given file name.
        """
        self.files_collection = MegaDB().db['files']

    async def insert_new_files(self, file_name: str, msg_id: int, chat_id: int, url: str,
                               file_type: str):
        self.files_collection.insert_one(
            {
                "file_name": file_name,
                "msg_id": msg_id,
                "chat_id": chat_id,
                "url": url,
                "file_type": file_type
            }
        )

    async def count_files_by_url(self, url: str):
        return self.files_collection.count({"url": url})

    async def get_file_by_url(self, url: str):
        return self.files_collection.find({"url": url})

    async def get_file_by_file_id(self, file_id: str):
        return self.files_collection.find_one({"_id": ObjectId(file_id)})

    async def get_file_by_name(self, file_name: str, row_limit: int):
        return self.files_collection.find({"file_name": re.compile(file_name, re.IGNORECASE)}).limit(row_limit)
