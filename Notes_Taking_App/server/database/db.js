import mongoose  from 'mongoose';

const Connection = async (username = 'user', password = '12345') => {
    const URL = `mongodb://${username}:${password}@ac-scinpx9-shard-00-00.60uu032.mongodb.net:27017,ac-scinpx9-shard-00-01.60uu032.mongodb.net:27017,ac-scinpx9-shard-00-02.60uu032.mongodb.net:27017/?ssl=true&replicaSet=atlas-4giamk-shard-0&authSource=admin&retryWrites=true&w=majority`;

    try {
        await mongoose.connect(URL, { useUnifiedTopology: true, useNewUrlParser: true });
        console.log('Database connected successfully');
    } catch (error) {   
        console.log('Error while connecting with the database ', error);
    }
}

export default Connection;