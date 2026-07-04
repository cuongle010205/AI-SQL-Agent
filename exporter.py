from io import BytesIO

def export_excel(df):

    buffer=BytesIO()

    df.to_excel(buffer,index=False)

    return buffer