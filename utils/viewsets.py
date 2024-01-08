from   fastapi        import HTTPException
from   starlette      import status
from   sqlalchemy.orm import Session



async def create_factory_method(
    model_name     : str, 
    request_schema : dict,
    db             : Session
):
    """
    Summary:
        this method will create a new object in the given model_name(table) 
        with all fields(request_schema)  
        
    Args:
        model_name     : create a new record in the given model_name 
        request_schema : fields (or) column value used to create a new object 
        created_by_id  : field to identify who created the object 
        db             : session variable to connect to database

    Raises:
        HTTPException  : HTTP_400_BAD_REQUEST if failed to create a new record
        
    Returns:
        object         : newly created object       
    """
    try:
        model_object    = model_name(**request_schema)
        db.add(model_object)
        db.commit()
        return model_object
    
    except Exception as e:
        raise HTTPException(
            status_code  =  status.HTTP_400_BAD_REQUEST,
            detail       =  f"{e}"
        )





def get_object_or_404(model_name, model_id, db):
    """
    Summary:
        this method will get a single object in the given model_name(table) 
        
    Args:
        model_name     : table_name (or) model_name to get the object
        model_id       : id field to uniquely identify the object
        db             : session variable to connect to database

    Raises:
        HTTPException  : HTTP_404_NOT_FOUND if failed to get the object
        
    Returns:
        object         : model object with all fields
    """
    model_object        =  db.query(model_name).filter(model_name.id == model_id, model_name.is_removed.is_(False)).first()

    if not model_object:
        raise HTTPException(
            status_code =  status.HTTP_404_NOT_FOUND,
            detail      =  f"{model_name.__name__} Object with id {model_id} Doesn't exist"
        )
    return model_object