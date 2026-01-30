import strawberry
from starlette.datastructures import UploadFile
from strawberry.file_uploads import Upload

@strawberry.type
class Query():
    pass


@strawberry.type
class Mutation():
    pass

schema = strawberry.Schema(
    query=Query, 
    mutation=Mutation,
    scalar_overrides={UploadFile: Upload}
)