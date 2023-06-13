function deleteNoted(noteId){
    fetch("/delete-note",{
        method = "POST",
        body:JSON.stringify({noteId:notId}),
    }).then((_res)=>{
        window.location.href= "/";
    });
}