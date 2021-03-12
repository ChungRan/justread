import { useState } from 'react';

function Book(){
    let [state, setState] = useState<any>({
        cover : 'cover',
        title : 'title',
        author : 'author'
    })


    return(
        <div>{ state.title }</div>
    )
}

export default Book;